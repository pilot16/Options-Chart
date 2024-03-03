import json
from functions.convert_to_dataframe import convert_to_dataframe


def parse_history(data):
    data = json.loads(data)
    data = data['history']
    data.reverse()
    pd_data = convert_to_dataframe(data)
    return pd_data
