#1
def read_file_line_by_line(file_name):
    with open(file_name, 'r') as file:
        for line in file:
            print(line.strip())

read_file_line_by_line('text1.txt')

#2
import random

def read_random_line(file_name):
    with open(file_name, 'r') as file:
        lines = file.readlines()
    return random.choice(lines).strip()

print(read_random_line('text1.txt'))

#3
def count_uppercase_chars(file_name):
    with open(file_name, 'r') as file:
        return sum(1 for char in file.read() if char.isupper())

print(count_uppercase_chars('text1.txt'))

#4
def count_non_starting_lines(file_name):
    with open(file_name, 'r') as file:
        return sum(1 for line in file if not line.startswith('D'))

print(count_non_starting_lines('text1.txt'))

#5
def count_ending_words(file_name):
    with open(file_name, 'r') as file:
        return sum(1 for word in file.read().split() if word.endswith('f'))

print(count_ending_words('text1.txt'))
#6
def count_all_none(file_name):
    with open(file_name, 'r') as file:
        words = file.read().split()
        return words.count('all'), words.count('none')

print(count_all_none('text1.txt'))

#7
def count_word_frequency(file_name):
    with open(file_name, 'r') as file:
        words = file.read().split()
        word_freq = {}
        for word in words:
            word_freq[word] = word_freq.get(word, 0) + 1
        return word_freq

print(count_word_frequency('text1.txt'))

#8
def find_longest_word(file_name):
    with open(file_name, 'r') as file:
        words = file.read().split()
        return max(words, key=len)

print(find_longest_word('text1.txt'))
#9
def correct_content(file_name):
    with open(file_name, 'r') as file:
        content = file.read()
    return content.replace('B', 'J').replace('b', 'j')

print(correct_content('text1.txt'))

#10
def count_characters(file_name):
    with open(file_name, 'r') as file:
        content = file.read()
        a_count = content.count('A') + content.count('a')
        b_count = content.count('B') + content.count('b')
        return a_count, b_count

print(count_characters('text1.txt'))