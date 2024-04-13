from datetime import datetime
import pandas as pd

if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(data, *args, **kwargs):

    data['Date_reported']=pd.to_datetime(data['Date_reported'])
    
    print("Rows without New Cases", data['New_cases'].isnull().sum())    

    return data[data['New_cases'].notnull()]

@test
def test_output(output, *args):
    assert output['New_cases'].isnull().sum() ==0, 'There are registers without New Covid Cases' 
