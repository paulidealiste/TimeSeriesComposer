import click
from time_series_composer.time_series_composer import TimeSeriesComposer

click.echo(
    ''
)
click.echo(
    'TimeSeriesComposer - easy ploting and data processing for time series data')
click.echo(
    ''
)


@click.command()
@click.option('--tsjson', default='',  type=click.Path(exists=True))
def cli(tsjson):
    """Provides a cli for time series json data"""
    tsc = TimeSeriesComposer()
    tsc.read_ts_data_json(click.format_filename(tsjson))
