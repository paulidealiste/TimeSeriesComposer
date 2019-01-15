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
        ts = pd.read_json(path)
        ts['Datetime'] = pd.to_datetime(ts['Datetime'])
        ts = ts.set_index('Datetime')
        print(ts)
        self.plot_ts_data_png(ts['Data'])

    def plot_ts_data_png(self, ts):
        fig, ax = plt.subplots(figsize=(15, 7))
        tsplot = ts.plot(ax=ax)
        ax.xaxis.set_major_locator(mdates.HourLocator())
        ax.xaxis.set_major_formatter(mdates.DateFormatter('%d %H:%M'))
        figure = tsplot.get_figure()
        figure.savefig("tsdata.png")
