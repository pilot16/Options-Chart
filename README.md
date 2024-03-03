
# Aevo Options Charts (WIP)

This project is designed to fetch histroical data options mark price data from the Aevo API, with customizable time intervals between each entry(30s, 60s, 5min, 15min, 30min, 1hr) and chart the price over time with the lightweight-charts library.

# Install
```
python -m venv .venv # Create a virtural environment
./.venv/Scripts/activate # Activate the venv

pip install lightweight-charts
pip install requests
```
# Displaying charts
After the project is installed, all you have to do is run the main.py, press Ctrl-F and search for a specific instrument, for example "ETH-04MAR24-3400-C".
![Search](https://github.com/pilot16/Options-Chart/blob/main/images/search.png?raw=true)
Press enter and you will see the fetched price data for the specific instrument.
![Search](https://github.com/pilot16/Options-Chart/blob/main/images/display.png?raw=true)
You can then change the timeframe, or search for new instruments.
If you're unsure of the different options instruments and names, the function "fetch_instrument_names" can be used to write a file with all the available assets.
