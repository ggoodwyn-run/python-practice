### Day 1

## Drill 1 - return number of vowels in a string

# My solution
def count_vowels(s):
    vowels = ["a", "e", "i", "o", "u"]
    number = 0
    for vowel in vowels:
        if vowel in s:
            amount = s.count(vowel)
            number += amount
    return number
    
number = count_vowels("hello world")
print(number)

# Best Solution

def count_vowels(s):
    vowels = ["a", "e", "i", "o", "u"]
    s = s.lower()
    total = 0

    for vowel in vowels:
        total += s.count(vowel)

    return total

# Best for coderbyte
def count_vowels(s):
    vowels = set("aeiou")
    total = 0

    for ch in s.lower():
        if ch in vowels:
            total += 1
    
    return total


vowels = set("aeiou")
print(vowels)


## Drill 2 - Reverse String

# My solution
def reverse_string(s):
    reversed = " "
    for i in range(1, len(s) + 1):
        reversed = reversed + s[-i]

    
    return reversed.strip()

## Drill 3 - character frequency (hash map pattern)

def char_frequency(s):
    freq = {}
    for l in s:
        freq[l] = freq.get(l, 0) + 1
    return freq

frequency = char_frequency('apple')
print(frequency) 


## Drill 4 - First non-repeating character

def first_unique_char(s):
    freq = {}
    for l in s:
        freq[l] = freq.get(l,0) + 1
    
    for l in s:
        if freq.get(l) == 1:
            return l
    return None

string = "aabbccddeefg"
first_unique_char(string)


## Day 2 - Drills

# Max in list, no max()


nums = [-1,-2,-3,-10,-5,-6,-12]

# My solution
def max_in_list(nums: list):
    max_number = nums[0]
    for i in nums:
        if i > max_number:
            max_number = i
    return max_number        
max_in_list(nums)

# Best Solution

def max_in_list(nums: list):
    max_number = nums[0]
    for i in nums[1:]:
        if i > max_number:
            max_number = i
    return max_number

# Sum the list

# My Solution

def sum_list(nums):
    total = 0
    for num in nums:
        total = total + num
    return total


numbers = [3,3,1]
print(sum_list(numbers))



# Palidrome check

def is_palindrome(s):
    s = s.lower().replace(" ", "")
    new_word = ""
    for i in range(1, len(s) + 1):
        new_word = new_word + s[-i]

    if new_word == s:
        True


word = "Race"