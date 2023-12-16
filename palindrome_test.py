import unittest

from palindrome import is_palindrome


class TestIsPalindrome(unittest.TestCase):
    def setUp(self):
        self.test_cases = [
            ("A man a plan a canal Panama", True),
            ("radar", True),
            ("Noon", True),
            ("hello", False),
            ("Able was I ere I saw Elba", True),
            ("", True),
            ("12321", True),
            ("python", False),
            ("No lemon, no melon", True),
            ("Was it a car or a cat I saw?", True),
            ("Palindrome", False),
        ]

    def test_is_palindrome(self):
        for input_str, expected_result in self.test_cases:
            with self.subTest(input_str=input_str, expected_result=expected_result):
                result = is_palindrome(input_str)
                self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()
