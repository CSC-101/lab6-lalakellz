import data
from typing import Optional
from data import Book
# Write your functions for each part in the space below.

# Part 0

# Finds the index of the smallest value in the list
# input: a list of integers
# input: a starting index
# returns: index of smallest value as an int or None if no value is found
def index_smallest_from(values:list[int], start:int) -> Optional[int]:
    if start >= len(values) or start < 0:
        return None

    mindex = start
    for idx in range(start + 1, len(values)):
        if values[idx] < values[mindex]:
            mindex = idx

    return mindex


# Sorts, in place, the elements of a list using the selection sort algorithm.
# input: a list of integers
# returns: nothing is returned; the list is sorted in place
#    <This function modifies/mutates the input list. Though a traditional
#     approach, cloning the list sorting the clone is potentially less
#     surprising. Or even using a different sorting algorithm.>
def selection_sort(values:list[int]) -> None:
    for idx in range(len(values) - 1):
        mindex = index_smallest_from(values, idx)
        tmp = values[mindex]
        values[mindex] = values[idx]
        values[idx] = tmp


# Part 1
# function to sort a list of Book objects by title
# input: list of Book objects
# output: None (sorts list in place)
def selection_sort_books(books: list[Book]) -> None:
    # go through each book in the list
    for i in range(len(books)):
        # assumes the current index is the minimum
        min_index = i

        # compare with the rest of the list
        for j in range(i + 1, len(books)):
            # if the title of the book at j is less than the title of the book at min_index
            if books [j].title < books[min_index].title:
                min_index = j
        # swap the found minimum title book with the book at index i
        books[i], books[min_index] = books[min_index], books[i]

# Part 2
# function to swap the case of each alphabetic character in a string
# input: a single string
# output: a string with uppercase characters converted to lowercase and lowercase characters converted to uppercase
def swap_case(input_str)-> str:
    result = ""
    for char in input_str:
        if char.islower():
            # convert lowercase to uppercase
            result += char.upper()
        elif char.isupper():
            # convert uppercase to lowercase
            result += char.lower()
        else:
            # non alphabetic characters remain the same
            result += char
    return result

# Part 3
# function to replace a character in a string with another character
# input: a string to modify, a character to replace, and a character to replace with
# output: a new string with specified replacements
def str_translate(input_str: str, old: str, new: str) -> str:
    result = ""
    for char in input_str:
        if char == old:
            # replace old with new
            result += new
        else:
            # leave other characters unchanged
            result += char
    return result

# Part 4
# function to create a word count histogram from a string
# input: a single string
# output: a dictionary mapping each word to its count in the string
def histogram(input_str: str) -> dict:
    word_counts = {}
    # split the string into words by spaces
    words = input_str.split()
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    return word_counts
