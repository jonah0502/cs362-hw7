import leapYear
import unittest

class leapyearTestCase(unittest.TestCase):
    def test_1(self):
        self.assertEqual(leapYear.isLeapYear(2150),False)
    
    def test_2(self):
        self.assertEqual(leapYear.isLeapYear(2140),True)

    def test_3(self):
        self.assertEqual(leapYear.isLeapYear(2000),True)

    def test_4(self):
        self.assertEqual(leapYear.isLeapYear(2200),False)
        
if __name__ == "__main__":
    unittest.main()