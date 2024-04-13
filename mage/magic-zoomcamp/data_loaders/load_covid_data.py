
import io
import pandas as pd
import requests
if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_data_from_api(*args, **kwargs):
    """
    Template for loading data from API
    """
    url = 'https://covid19.who.int/WHO-COVID-19-global-data.csv'
    response = requests.get(url)

    covid_dtypes = { 
                    'Country_code': str,
                    'Country': str,
                    'WHO_region': str,
                    'New_cases': pd.Int64Dtype(),
                    'Cumulative_cases': pd.Int64Dtype(),
                    'New_deaths': pd.Int64Dtype(),
                    'Cumulative_deaths': pd.Int64Dtype()
                }
    parse_dates=['Date_reported']
    return pd.read_csv(io.StringIO(response.text), sep=',', dtype=covid_dtypes, encoding = 'utf-8', parse_dates=parse_dates)

@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'