import data
from typing import Optional
from data import Book
# Write your functions for each part in the space below.

# Part 0

# Finds the index of the smallest value in the list, if there are values,
#     starting from the provided index (if in bounds).
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
# Function to sort a list of Book objects by title using selection sort
# input: list of Book objects
# output: None (sorts list in-place)
def selection_sort_books(books: list[Book]) -> None:
    # Iterate through each book in the list
    for i in range(len(books)):
        # Assume the current index is the minimum
        min_index = i

        # Compare with the rest of the list
        for j in range(i + 1, len(books)):
            # If the title of the book at j is less than the title of the book at min_index
            if books [j].title < books[min_index].title:
                min_index = j
        # Swap the found minimum title book with the book at index i
        books[i], books[min_index] = books[min_index], books[i]

# Part 2
# Function to swap the case of each alphabetic character in a string
# input: a single string
# output: a string with uppercase characters converted to lowercase and lowercase characters converted to uppercase
def swap_case(input_str)-> str:
    result = ""
    for char in input_str:
        if char.islower():
            # Convert lowercase to uppercase
            result += char.upper()
        elif char.isupper():
            # Convert uppercase to lowercase
            result += char.lower()
        else:
            # Non-alphabetic characters remain the same
            result += char
    return result

# Part 3


# Part 4
