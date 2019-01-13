from .context import time_series_composer
import os


def test_tsc_read(capsys):
    tsc = time_series_composer.TimeSeriesComposer()
    basePath = os.path.dirname(os.path.abspath(__file__))
    tsc.read_ts_data_json(basePath + "/tsdump.json")
    out, err = capsys.readouterr()
    open(basePath + "/err.txt", "w").write(err)
    open(basePath + "/out.txt", "w").write(out)
