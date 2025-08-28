import unittest

from src.Chapter03.myfile import myfile


class TestChapter03(unittest.TestCase):
    def test_myfile_title(self):
        expected_title = 'Learning Python, 6th Edition'
        self.assertEqual(myfile.title, expected_title)


if __name__ == '__main__':
    unittest.main()