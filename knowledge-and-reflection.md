# Overview

These questions are designed to accompany the task "Implementing a Hash Map in Python" in the "Data Structures and Algorithms" module. The questions are intended to test your understanding of hash maps, their implementation in Python, and the process of integrating data from a double linked list into a hash map. You will also be asked to reflect on your learning and the challenges you faced during the task.

# Knowledge questions

The following are all examples of hash functions:

```python
# (1) the simplest hash function (Stupidly Simple Hash)
def ssh(key):
    return 1
```

```python
# (2) hash function that sums the ASCII values of the characters in the key
def sum_of_ascii_values(key: str, size: int) -> int:
    total = 0
    for char in key:
        total += ord(char)
    return total % size
```

A more Pythonic version

```python
# (2a)
def sum_of_ascii_values(key: str, size: int) -> int:
    return sum(ord(char) for char in key) % size
```

A Pearson Hash function

```python
# (3) Pearson hash function
# https://en.wikipedia.org/wiki/Pearson_hashing
import random

random.seed(42)

# This is INCORRECT:
# pearson_table = [random.randint(0, 255) for _ in range(256)]
pearson_table = list(range(256))
random.shuffle(pearson_table)

def pearson_hash(key: str, size: int) -> int:
    hash_ = 0
    for char in key:
        hash_ = pearson_table[hash_ ^ ord(char)]
    return hash_ % size
```

The following is a hash function that uses the built-in `hash` function in Python

```python
# (4) hash function that uses the built-in hash function
def built_in_hash(key: str, size: int) -> int:
    return hash(key) % size
```

Finally, the following is a hash function that uses the `SHA256` hash function from the `hashlib` module

```python
# (5) hash function that uses the SHA256 hash function
# https://docs.python.org/3/library/hashlib.html
# https://en.wikipedia.org/wiki/SHA-2
# https://en.wikipedia.org/wiki/SHA-2#Pseudocode
import hashlib

def sha256_hash(key: str, size: int) -> int:
    return int(hashlib.sha256(key.encode()).hexdigest(), 16) % size
```

1. All of the above functions are hash functions. Explain how so - what key properties do they all share?

> Each function takes in a 'key' parameter (typically a string), hashes the key, and returns a hash value of type int.
> Apart from the first hash function above, hash functions typically take in an extra 'size' parameter of type int.

2. What are the advantages and disadvantages of each of the above hash functions? Evaluate in terms of uniformity, determinism, efficiency, collision resistance, sensitivity to input changes, and security[1](#Reference). You may need to do some reasearch to answer this question 😱

> **HASH FUNCTION (1)**
> - Advantages
>   - Very efficient, constant time complexity O(1).
>   - Deterministic, it produces the same output for a given input.
> - Disadvantages
>   - Not uniform, hash values are not evenly distributed based on the given hash map size.
>   - Not resistant to collision as each hash value will result to 1.
>   - Not sensitive to input changes as per point above.
>   - Not secure as output is predictable after producing a few hashes for different inputs.
> 
> **HASH FUNCTION (2)**
> - Advantages
>   - Deterministic, it produces the same output for a given input.
>   - Sensitive to input changes.
> - Disadvantages
>   - Does not uniformly distribute hash values. If hash map size is small compared to 'total' then the hash function would do a good job at evenly distributing the hash values.
>   - Not resistant to collisions due to point above.
>   - Not as efficient since each character is being looped, time will increase if length of key input increases, hence time complexity is O(n).
>   - Not secure since it is less resistant to collisions.
> 
> **HASH FUNCTION (3)**
> - Advantages
>     - Deterministic, it produces the same output for a given input.
>     - Efficient especially for processors with 8-bit registers. However, time complexity is O(n) due to looping over each character in key input.
>     - Uniform distribution of hash values for the given hash map.
>     - Sensitive to input changes, where two input strings that differ by one character will never produce the same hash value.
>     - Resistant to collisions.
> - Disadvantages
>   - Not secure in a cryptographic sense.
> 
> **HASH FUNCTION (4)**
> - Advantages
>   - Computationally efficient. However, time complexity is O(n) due to input size.
>   - Uniform distribution of hash values for the given hash map.
>   - Sensitive to input changes, where two input strings that differ by one character will never produce the same hash value.
>   - Secure as hash values are unpredictable and random.
> - Disadvantages
>   - Not deterministic. Python's inbuilt hash function returns different hash values when invoked multiple times. It is only the same for a single instance
>   and is commonly used to quickly compare dictionary keys during a dictionary lookup. Hence, the hash values are not suitable to be stored externally.
>   - Not resistant to collisions since hash() returns a fixed-sized output regardless of the input size. By having an input that is larger in size than
>   the output can cause a collision.
> 
> **HASH FUNCTION (5)**
> - Advantages
>   - Uniform distribution of hash values for the given hash map.
>   - Sensitive to input changes, where two input strings that differ by one character will never produce the same hash value.
>   - Computationally efficient, although time complexity is O(n).
>   - Deterministic as it produces the same output for a given input.
>   - Resistant to collisions such that it is computationally impractical to find two different input strings with the same hash value.
>   - Secure as it produces an irreversible hash value.
> - Disadvantages
>   - For non-cryptographic use, the function is less efficient when compared to other hashing functions such as MD5.

3. List the three most important attributes (arranged from most to least) in the context of a hash map? Justify your answer.

> 1. Hash function that is resistant to collisions.
> 2. Size of hash map.
> 3. Collision handling (Chaining and Open Addressing)

4. Which of the above hash functions would you choose to implement the requirements of the task? Why?

> Function (5) which uses the SHA256 hash function from hashlib module. Firstly, it is an industry standard that is trusted by
> leading public-sector agencies and used widely by technology leaders. The algorithm doesn't have any known vulnerabilities that
> make it insecure. Besides that, collisions are very unlikely to occur due to the possible combinations of hash values (2**256) 
> when using this hash function. In addition, the hash function is irreversible and computational effort is relatively fast for this application.

5. In your own words, explain each line in the pearson hash function above in terms of the criteria you listed in question 2.

> The random module is imported and a seed of 42 is passed to random's seed function that will be used to generate the pearson_table.
> The pearson hash function uses a 256-byte lookup table containing permutations of the values 0-255.
> In the first line of the pearson_hash function, a hash variable is initialised to 0.
> The second line of the pearson_hash function is a for loop that loops over each character in the key input, in which the looping operation
> may be computationally inefficient for large sizes of key. Because of this, time complexity of the hash function is O(n).
> The third line of the pearson_hash function is re-assigning hash_ based on the pearson_table lookup. The time complexity for this line is O(1). In addition, this line proves that the function is deterministic where the output is always the same for a given input.
> The fourth line of the pearson_hash function returns the hash value that falls within the range of the size variable. If size is smaller than hash_ then the hash values would be distributed uniformly and vice versa.

6. Write pseudocode of how you would store Players in PlayerLists in a hash map.

> 1. Get the hash value from Player by hashing the Player key.
> 2. Use hash value from (1) to determine the corresponding PlayerList in the hash map.
> 3. Check if PlayerList is empty, if it is then add Player to PlayerList found in (2).
> 4. If PlayerList is not empty AND Player key is not in PlayerList, then add Player to PlayerList.
> 5. If PlayerList is not empty AND Player key is in PlayerList, locate Player and update Player name.

## Reflection

1. What was the most challenging aspect of this task?

> Implementing a custom hash function by overriding __hash__ dunder method. If hashing a player by calling hash(player_node),
> then the hash will be truncated based on the bit width of my machine. To address this, I added a modulo operator on the returned
> integer digest with the modulus value (sys.hash_info.modulus).

2. If you didn't have to use a PlayerList, how would you have changed them implementation of the hash map and why?

> Instead of using PlayerList which is a double linked list that utilises PlayerNode, I will use Player objects and implement open addressing to handle collisions.
> 

## Reference

### Key Dimensions of Hash Functions

1. **Uniformity**: the probability of any given hash value within the range of possible hash values should be approximately equal.

2. **Determinism**: a given input will always produce the same output.

3. **Efficiency**: the time complexity of computing the hash value should be constant, the hash function should be fast to compute, and utilize the architecture of the computer effectively

4. **Collision Resistance:** minimize the probability of collisions, through a variety of mechanisms.

5. **Sensitivity to input changes:** small changes in the input should produce large changes in the output.

6. **Security**
   - It should be computationally infeasible to find an input key that produces a specific hash value (non-reversibility)
   - The output hash values should appear random and unpredictable.
