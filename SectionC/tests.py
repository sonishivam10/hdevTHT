from say_the_number import SectionC
import unittest

class TestSayTheNumber(unittest.TestCase):

    #Initilize object for SectionC class
    testClass = SectionC()

    def test_suite1(self):
        assert self.testClass.sayNumber(0)=="Zero."

    def test_suite2(self):
        assert self.testClass.sayNumber(11)=="Eleven."

    def test_suite3(self):
        assert self.testClass.sayNumber(90376000010012)=="Ninety trillion, three hundred and seventy six billion, ten thousand and twelve."



