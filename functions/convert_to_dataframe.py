import pandas as pd
from datetime import datetime, timezone


def convert_to_dataframe(data):
    for i in range(len(data)):
        data[i].insert(0, i)
    data_df = pd.DataFrame(data, columns=["", 'time', 'price'])
    data_df['time'] = [datetime.fromtimestamp(int(t) / 1e9, tz=timezone.utc).astimezone() for t in data_df['time']]
    data_df.set_index('time', inplace=True)
    data_df['price'] = data_df['price'].astype(float)
    return data_df
