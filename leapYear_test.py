import leapYear
import unittest

class leapyearTestCase(unittest.TestCase):
    def test_normalyear(self):
        self.assertEqual(leapYear.isLeapYear(1),True)
        
if __name__ == "__main__":
    unittest.main()