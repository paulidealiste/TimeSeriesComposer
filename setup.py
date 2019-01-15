from setuptools import setup, find_packages

setup(
    name="TimeSeriesComposer",
    description="Simple cli interface for time series pandas plots",
    version="0.1",
    include_package_data=True,
    py_modules=['tscomposer', 'time_series_composer'],
    packages=find_packages(exclude=['tests']),
    install_requires=[
        'click',
        'numpy',
        'pandas',
        'matplotlib'
    ],
    entry_points={
        'console_scripts': [
            'tscomposer = tscomposer:cli'
        ],
    }
)
