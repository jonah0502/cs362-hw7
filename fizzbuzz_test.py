import fizzbuzz
import unittest

class fizzbuzzTestCase(unittest.TestCase):
    def test_divisibleByThree(self):
        self.assertEqual(fizzbuzz.fizzbuzz(3),"Fizz")


if __name__ == "__main__":
    unittest.main()