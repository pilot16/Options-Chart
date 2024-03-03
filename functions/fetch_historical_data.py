import requests


def fetch_historical_data(instrument, timeframe):
    if timeframe == 0:
        timeframe = 30
    limit = 1000

    url = f"https://api.aevo.xyz/mark-history?instrument_name={instrument}&resolution={timeframe}&limit={limit}"
    headers = {"accept": "application/json"}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        print(f"Request failed: {e}")
        return
