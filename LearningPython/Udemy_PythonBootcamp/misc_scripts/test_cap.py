import unittest
import cap

class TestCap(unittest.TestCase):

    # test for any thing that might come to my mind
    def test_one_word(self):
        text = 'Python'
        result = cap.cap_text(text)
        self.assertEqual(result,'Python')

    def test_multiple_words(self):
        text = 'monty python'
        result = cap.cap_text(text)
        self.assertEqual(result,'Monty Python')

if __name__ == '__main__':
    unittest.main()
