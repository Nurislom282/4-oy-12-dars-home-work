#1
lines = ["Hello", "World", "Python", "Programming"]
letter_counts = list(map(lambda s: len(s), lines))
print(letter_counts)
#2
numbers = [1, 2, 3, 4, 5]
multiplied_numbers = list(map(lambda x: x * 3, numbers))
print(multiplied_numbers)
#3
list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8]
result = list(map(lambda x, y: x + y, list1, list2))
print(result)
#4
sentences = ["Bu birinchi jumla", "Ikkinchi jumla", "Uchinchi jumla"]
def get_last_letters(sentence):
    return [word[-1] for word in sentence.split()]
last_letters = list(map(get_last_letters, sentences))
print(last_letters)
#5
numbers = [12, 25, 37, 49, 58]
result = list(map(lambda x: x % 10, numbers))
print(result)
#6
import math
numbers = [1, 4, 9, 16, 25]
square_roots = list(map(math.sqrt, numbers))
print(square_roots)
#7
numbers = [3, 6, 9, 12, 15]
result = list(map(lambda x: x / 10, filter(lambda x: x > 5, numbers)))
print(result)
#8
variables = ['var1', 'var2', 'var3']
uppercase_vars = list(map(str.upper, variables))
print(uppercase_vars)
#9
a, b = 5, 10
max_value = max(a, b)
print(max_value)
#10
numbers = [2, 4, 6, 8]
multiplied = list(map(lambda x: x * 1, numbers))
print(multiplied)
#11
list1 = [1, 2, 3]
list2 = [4, 5, 6]
sum_of_squares = list(map(lambda x, y: x**2 + y**2, list1, list2))
print(sum_of_squares)
#12
numbers = [5, 12, 99, 100, 45]
two_digit_numbers = list(filter(lambda x: 10 <= x < 100, numbers))
print(two_digit_numbers)
#13
words = ['apple', 'banana', 'orange', 'umbrella']
vowel_words = list(filter(lambda word: word[0].lower() in 'aeiou', words))
print(vowel_words)
#14
strings = ['hello', '', 'world', '', 'python']
non_empty_strings = list(filter(lambda s: s != '', strings))
print(non_empty_strings)
#15
import re
strings = ['abc123', 'def456', 'ghi789']
numbers = list(map(lambda s: re.findall(r'\d+', s), strings))
print(numbers)
#16
numbers = [50, 150, 200, 75, 125]
greater_than_100 = list(filter(lambda x: x > 100, numbers))
print(greater_than_100)
#17
numbers = [10, 20, 110, 210, 30, 410]
result = list(filter(lambda x: str(x).endswith('10'), numbers))
print(result)
#18
words = ["level", "world", "radar", "python", "madam"]
result = list(filter(lambda x: x == x[::-1], words))
print(result)
#19
names = ["Alice", "BOB", "CHARLIE", "dave"]
result = list(filter(lambda x: x.isupper(), names))
print(result)
#20
words = ["cat", "dog", "elephant", "bat", "ant"]
result = list(filter(lambda x: len(x) == 3, words))
print(result)
#21
numbers = [-10, 20, -30, 40, 50]
result = list(filter(lambda x: x > 0, numbers))
print(result)
#22
numbers = [3, 23, 35, 40, 300, 13]
result = list(filter(lambda x: str(x).startswith('3'), numbers))
print(result)