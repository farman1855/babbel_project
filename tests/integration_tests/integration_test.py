from unittest import TestCase
import sys
import os
sys.path.append(".")
from module.helpers import Helpers
import requests


class UnitTest(TestCase):
    def test_get_path(self):
        path = Helpers.get_path().strip()
        path1 = os.getcwd().strip()
        self.assertEqual(path, path1)

    def test_get_rate(self):
        config = Helpers.get_config()
        url = config['url']
        response = requests.get(url)
        data = response.json()
        self.assertEqual(Helpers.get_rate(), data)