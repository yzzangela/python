# START PROBLEM SET 01
print('Problem Set 01')

# PROBLEM 1 (20 points)
print('\nProblem 1')

#python author = "Guido van Rossum"
#python_author = Guido van Rossum
python_author = "Guido van Rossum"
python_current_version = "3.8.5"
#'3.8.5' = python_version

valid_variables = [python_author, python_current_version]

print(f"\nValid = {valid_variables}")

# PROBLEM 2 (20 points)
print('\nProblem 2')

# PROBLEM 2 SETUP
# Please do not change.

name = "Guido van Rossum"
python_foundation_officers = ['Guido van Rossum', 'Lorena Mesa', 'Thomas Wouters']
zen_of_python = """
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
"""
# END PROBLEM 2 SETUP

name_type = type(name)
officers_type = type(python_foundation_officers)
zen_type = type(zen_of_python)

print(name_type)
print(officers_type)
print(zen_type)
num_chars_zen =len(zen_of_python)

# PROBLEM  3 (20 points)
print('\nProblem 3')

num_words = len(str.split(zen_of_python))
avg_words = num_words/19

print(f"\nNumber of words = {num_words}")
print(f"\nAverage number of words per line = {avg_words}")

# PROBLEM 4 (20 points)
print('\nProblem 4')

total_words = (num_words + avg_words)

print(f"\nNew total number of words in Zen of Python = {total_words}")


# PROBLEM 5 (20 points)
print('\nProblem 5')

num_chars_zen = len(zen_of_python)

print(f"\nNumber of characters = {num_chars_zen}")

avg_chars = (num_chars_zen//num_words)

print(f"\nAverage number of characters per word = {avg_chars}")
