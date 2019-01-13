import pandas as pd


class TimeSeriesComposer(object):
    '''JSON based time series data methods under one roof
    Attributes:
    '''

    _time_series_frame = pd.DataFrame()

    def __init__(self):
        pass

    def read_ts_data_json(self, path):
        ts = pd.read_json(path)
        print(ts)
