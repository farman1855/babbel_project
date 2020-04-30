from unittest import TestCase
import sys
import os
sys.path.append(".")
from module.helpers import Helpers
import pandas as pd


class UnitTest(TestCase):
    def test_get_path(self):
        data = Helpers.get_rate()
        df = Helpers.get_dataframe(data)
        self.assertEqual(list(df.columns),list(pd.read_csv(os.getcwd()+'/data/test.csv',nrows=1).columns))


