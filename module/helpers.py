import json
import os
from datetime import datetime

import pandas as pd
import requests
from pandas.io.json import json_normalize


class Helpers:
    def get_path():
        path = os.getcwd()
        return path

    def get_config():
        with open(Helpers.get_path() + '/config/config.json') as config_file:
            data = json.load(config_file)
            return data

    def get_rate():
        config = Helpers.get_config()
        url = config['url']
        response = requests.get(url)
        data = response.json()
        return data

    def get_dataframe(data):
        df = json_normalize(data)
        df.columns = df.columns.str.replace("conversion_rates.", "")
        df.drop(
            [
                "base",
                "result",
                "documentation",
                "terms_of_use",
                "time_next_update",
                "time_zone",
            ],
            axis=1,
            inplace=True,
        )
        df.insert(
            0,
            "update_time",
            datetime.utcfromtimestamp(df["time_last_update"]).strftime("%H:%M:%S"),
            True,
        )
        df["time_last_update"] = pd.to_datetime(df["time_last_update"], unit="s").dt.date
        df.rename(columns={"time_last_update": "update_date"}, inplace=True)
        cols = list(df.columns)
        cols = [cols[-1]] + cols[:-1]
        df = df[cols]
        return df

    def write_data(df):
        filename = os.path.dirname(Helpers.get_path()) + "/data/exchangerate.csv"
        if not os.path.isfile(filename):
            df.to_csv(filename, header="column_names", index=False)
        else:
            df.to_csv(filename, mode="a", header=False, index=False)
