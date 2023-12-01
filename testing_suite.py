"""
@author: https://github.com/Divyateja04
"""
import unittest
from sophos_scraper import get_data_left, Browser, login_into_sophos
import json

class TestScraper(unittest.TestCase):
    def test_data_left(self):
        with open("data.json") as f:
            data = json.load(f)
            val = get_data_left(data["username"], data["password"], Browser.Firefox)
            self.assertTrue(val)
    
    def test_auto_login(self):
        with open("data.json") as f:
            data = json.load(f)
            val = login_into_sophos(data["username"], data["password"])
            self.assertTrue(val)

if __name__ == "__main__":
    unittest.main()
