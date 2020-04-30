# -*- coding: utf-8 -*-
import os
import sys


sys.path.append(os.getcwd()+"/helpers.py")
from helpers import Helpers


def main():
    data = Helpers.get_rate()
    df = Helpers.get_dataframe(data)
    Helpers.write_data(df)

if __name__ == '__main__':
    main()

