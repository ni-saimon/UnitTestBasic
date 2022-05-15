import unittest
from selenium import webdriver
import page


class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r"C:\Users\nafiz\Downloads\chromedriver.exe")
        self.driver.get("http://www.python.org")

    def test_example(self):
        assert True

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()