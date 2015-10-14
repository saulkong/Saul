__author__ = 'xiaocong'

import pandas as pd

class TimeSeries(object):
    all=pd.read_csv('/Users/xiaocong/Downloads/datasource/timeseries_data_file.csv',parse_dates=True,index_col=0)
    all=all.resample('B',fill_method='ffill')
    all['AAPL'].plot()
    all['MSFT'].plot()
    all['XOM'].plot()
    all['SPX'].plot()


def main():
    TimeSeries()

if __name__=='__main__':
    main()