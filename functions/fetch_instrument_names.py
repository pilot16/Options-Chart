import json
import requests


def get_instrument_names(data):
    data = json.loads(data)
    instruments = [{"instrument_name": element["instrument_name"]} for element in data]
    with open("../instruments.json", "w") as file:
        json.dump(instruments, file)
    return


def fetch_market_data():
    url = "https://api.aevo.xyz/markets?instrument_type=OPTION"
    headers = {"accept": "application/json"}
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        print(f"Request failed: {e}")
        return
