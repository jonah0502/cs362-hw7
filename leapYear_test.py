import leapYear
import unittest

class leapyearTestCase(unittest.TestCase):
    def test_1(self):
        self.assertEqual(leapYear.isLeapYear(2150),False)
    
    def test_2(self):
        self.assertEqual(leapYear.isLeapYear(2140),True)
        
if __name__ == "__main__":
    unittest.main()