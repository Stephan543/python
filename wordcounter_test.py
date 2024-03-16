import unittest
import wordcounter

class TestTextClass(unittest.TestCase):
    def test_count_string(self):
        test_cases = {
            ("Hello", 1),
            ("Hello Hello", 2),
            (" Hello World ", 2),
            ("", 0),
            ("   ", 0),
            (" word a    s   ", 3)
        }
    
        for text, expected_count in test_cases:
            with self.subTest(text=text):
                text_obj = wordcounter.Text(text)
                self.assertEqual(text_obj.count_string(), expected_count)
            
if __name__ == '__main__':
    unittest.main()