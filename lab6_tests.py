import data
import lab6
import unittest
from data import Book
from lab6 import selection_sort_books,swap_case, str_translate, histogram

# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 0
    def test_index_smallest_from_1(self):
        input = [2, 1, 9, 0, 4, 5]
        expected = 3
        actual = lab6.index_smallest_from(input, 0)
        self.assertEqual(expected, actual)


    def test_index_smallest_from_2(self):
        input = [2, 1, 9, 0, 4, 5]
        expected = 4
        actual = lab6.index_smallest_from(input, 4)
        self.assertEqual(expected, actual)


    def test_index_smallest_from_3(self):
        input = [2, 1, 9, 0, 4, 5]
        expected = None
        actual = lab6.index_smallest_from(input, 6)
        self.assertEqual(expected, actual)


    def test_index_smallest_from_4(self):
        input = []
        expected = None
        actual = lab6.index_smallest_from(input, 0)
        self.assertEqual(expected, actual)


    def test_selection_sort_1(self):
        input = [1, 2, 3, 4, 5]
        expected = [1, 2, 3, 4, 5]
        lab6.selection_sort(input)
        self.assertEqual(expected, input)


    def test_selection_sort_2(self):
        input = []
        expected = []
        lab6.selection_sort(input)
        self.assertEqual(expected, input)


    def test_selection_sort_3(self):
        input = [9, 7, 5, 3, 1]
        expected = [1, 3, 5, 7, 9]
        lab6.selection_sort(input)
        self.assertEqual(expected, input)


    def test_selection_sort_4(self):
        input = [5, 0, 19, 21, 4, 6]
        expected = [0, 4, 5, 6, 19, 21]
        lab6.selection_sort(input)
        self.assertEqual(expected, input)


    # Part 1
    def test_sorted_books(self):
        books = [
            Book("J.D. Salinger", "The Catcher in the Rye"),
            Book( "George Orwell", "1984"),
            Book("Harper Lee", "To Kill a Mockingbird"),
            Book("George Orwell", "Animal Farm")
        ]
        expected_titles = [
            "1984", "Animal Farm", "The Catcher in the Rye", "To Kill a Mockingbird"
        ]
        selection_sort_books(books)
        sorted_titles = [book.title for book in books]
        self.assertEqual(sorted_titles, expected_titles)

    def test_empty_list(self):
        input_books = []
        selection_sort_books(input_books)
        self.assertEqual([], input_books)

    #Part 2
    def test_swap(self):
        input_str = "WHatsUp!"
        expected = "whATSuP!"
        self.assertEqual(swap_case(input_str), expected)

    def test_swap_2(self):
        input_str = "ĆaMaR"
        expected = "ćAmAr"
        self.assertEqual(swap_case(input_str), expected)

    def test_swap_3(self):
        input_str = "1234!@#$"
        expected = "1234!@#$"
        self.assertEqual(swap_case(input_str), expected)

    # Part 3
    def test_translate(self):
        input_str = "abcdcba"
        old = 'a'
        new = 'x'
        expected = "xbcdcbx"
        self.assertEqual(str_translate(input_str, old, new), expected)

    def test_translate_2(self):
        input_str = "aaaa"
        old = 'a'
        new = 'b'
        expected = "bbbb"
        self.assertEqual(str_translate(input_str, old, new), expected)

    # Part 4
    def test_case_sensitivity(self):
        input_str = "Dog dog DOG"
        expected = {'Dog': 1, 'dog': 1, 'DOG': 1}
        self.assertEqual(histogram(input_str), expected)

    def test_multiple_words_same_count(self):
        input_str = "apple banana apple banana"
        expected = {'apple': 2, 'banana': 2}
        self.assertEqual(histogram(input_str), expected)


if __name__ == '__main__':
    unittest.main()
