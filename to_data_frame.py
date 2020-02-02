# -*- coding: utf-8 -*-
"""
This function will export data taken from RNX file as 
an dictionary into simple pandas DataFame object with 
epoch of satellite observation as an index value
To test , it prints first 20 rows and DataFrame size.
It returns DataFrame named epochFrame.
"""
def to_pandas_DataFrame(satellites):
    import pandas as pd
    global epochFrame
    epochFrame = pd.DataFrame.from_dict(satellites,orient='index',dtype='float64')
    print('Number of columns in epochFrame:',len(epochFrame.columns))
    print('Number of rows in epochFrame:',len(epochFrame.index))
    print(epochFrame.head(100))
    return epochFrame
    