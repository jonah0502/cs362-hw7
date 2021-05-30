import leapYear
import unittest

class leapyearTestCase(unittest.TestCase):
    def test_leapYear(self):
        self.assertEqual(leapYear.isLeapYear(2150),False)
        
if __name__ == "__main__":
    unittest.main()