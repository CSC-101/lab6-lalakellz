import data
import lab6
import unittest
from data import Book
from lab6 import selection_sort_books,swap_case

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
    def test_multiple_books(self):
        # Test with multiple books
        books = [Book("1984"),
            Book("To Kill a Mockingbird"),
            Book("Brave New World"),
            Book("The Great Gatsby"),
            Book("Moby Dick")]
        selection_sort_books(books)
        sorted_titles = [book.title for book in books]
        expected_titles = sorted(sorted_titles)  # Get expected order by sorting titles
        self.assertEqual(sorted_titles, expected_titles)

    def test_empty_list(self):
        # Input: an empty list
        input_books = []

        # Act: sort the empty list
        selection_sort_books(input_books)

        # Assert: the empty list should remain empty
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


    # Part 4





if __name__ == '__main__':
    unittest.main()
