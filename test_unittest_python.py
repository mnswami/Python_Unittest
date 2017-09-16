import unittest
import logging
import xmlrunner

class my_unittest_framework(unittest.TestCase):
    def setupClass(cls):
        print("In set up class")
    def tearDownclass(cls):
        print("In tear down class")

    def setUp(self):
        print("in setup function")

    def tearDown(self):
        print("In tear down class")

    def test_1(self):
        self.assertTrue(2 >1)

    def test_2(self):
        self.assertEqual(2-3, 8)

if __name__ == '__main__':
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output='test-reports'))
