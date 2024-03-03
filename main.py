from lightweight_charts import Chart
from functions.fetch_historical_data import fetch_historical_data
from functions.parse_history import parse_history


def on_search(chart, instrument):
    timeframe = int(chart.topbar['timeframe'].value)
    data = fetch_historical_data(instrument, timeframe)
    data_df = parse_history(data)
    chart.lines()[0].set(data_df)
    chart.topbar["instrument"].set(instrument)


def on_timeframe(chart):
    instrument = chart.topbar["instrument"].value
    timeframe = int(chart.topbar['timeframe'].value)
    if instrument == "":
        print("No instrument selected")
        return
    data = fetch_historical_data(instrument, timeframe)
    data_df = parse_history(data)
    chart.lines()[0].set(data_df)


if __name__ == '__main__':
    chart = Chart()
    chart.legend(visible=True)

    chart.events.search += on_search

    chart.topbar.textbox('instrument', '')
    chart.topbar.switcher('timeframe', ("30", "60", "300", "900", "1800", "3600"), default="30",
                          func=on_timeframe)
    historical_line = chart.create_line("price", "white")
    chart.show(block=True)
