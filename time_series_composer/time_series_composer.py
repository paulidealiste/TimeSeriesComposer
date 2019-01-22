import json
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
import matplotlib.dates as mdates

plt.style.use('ggplot')
mpl.rc('lines', linewidth=1)
mpl.rc('font', size='8')


class TimeSeriesComposer(object):
    """JSON based time series data methods under one roof.

    Attributes:
    """

    _time_series_frame = pd.DataFrame()

    def __init__(self):
        pass

    def read_ts_data_json(self, path):
        with open(path) as timeseriesdata:
            read_data = json.load(timeseriesdata)
        timeserieslist = []
        for series_id in read_data.keys():
            ots = pd.DataFrame(read_data[series_id]['series_data'])
            ots['date_time'] = pd.to_datetime(ots['date_time'])
            ots = ots.set_index('date_time')
            ots.columns = [series_id, series_id + 'pid']
            timeserieslist.append(ots)
        timeseriesframe = pd.concat(timeserieslist, axis=1)
        print(timeseriesframe)
        self.plot_ts_data_png(timeseriesframe[list(read_data.keys())])

    def plot_ts_data_png(self, ts):
        fig, ax = plt.subplots(figsize=(15, 7))
        tsplot = ts.plot(ax=ax, marker="o")
        ax.xaxis.set_major_locator(mdates.HourLocator())
        ax.xaxis.set_major_formatter(mdates.DateFormatter('%d %H:%M'))
        figure = tsplot.get_figure()
        figure.savefig("tsdata.png")
