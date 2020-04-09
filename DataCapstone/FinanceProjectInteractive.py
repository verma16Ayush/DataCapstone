'''
import various libraries to be
used in this project
'''
import pandas as pd
import numpy as np
import datetime as dt
import pandas_datareader as dr
import matplotlib.pyplot as plt
import seaborn as sns

bank_stocks = pd.DataFrame()
returns = pd.DataFrame()
'''
creating a list object ticker and storing a list of all the tickers of the bank
in alphabetical order 
'''
tickers = ('BAC C GS MS JPM WFC'.split())
tickers.sort()


def default():
    '''
    reading bank stocks data off the internet
    for various banks.
    the datareader method identifies the bank name from its ticker. unfortunately google is not
    available for some reason. set the start and end as a datetime object
    '''
    bac = dr.data.DataReader('BAC', data_source='yahoo', start=dt.datetime(2006, 1, 1), end=dt.datetime(2016, 1, 1))
    c = dr.data.DataReader('C', data_source='yahoo', start=dt.datetime(2006, 1, 1), end=dt.datetime(2016, 1, 1))
    # sbin = dr.data.DataReader('SBIN',data_source='yahoo',start=dt.datetime(2006,1,1),end=dt.datetime(2016,1,1))
    gs = dr.data.DataReader('GS', data_source='yahoo', start=dt.datetime(2006, 1, 1), end=dt.datetime(2016, 1, 1))
    jpm = dr.data.DataReader('JPM', data_source='yahoo', start=dt.datetime(2006, 1, 1), end=dt.datetime(2016, 1, 1))
    ms = dr.data.DataReader('MS', data_source='yahoo', start=dt.datetime(2006, 1, 1), end=dt.datetime(2016, 1, 1))
    wfc = dr.data.DataReader('WFC', data_source='yahoo', start=dt.datetime(2006, 1, 1), end=dt.datetime(2016, 1, 1))



    # print(tickers)

    # create a new dataframe merging all the data of the banks
    bank_stocks = pd.concat([bac, c, gs, jpm, ms, wfc], axis=1, keys=tickers)

    # printing the head of the bank stocks dataframe
    # print(bank_stocks.head())

    # naming the two levels of columns
    bank_stocks.columns.names = ['Bank Ticker', 'Stock Info']

    # print the dataframe head again with new column indices
    print(bank_stocks.head())

    '''
    creating a new dataframe returns and storing the percentage change values of 
    of closing values of all the bAnks
    printing the head of the returns dataframe
    '''
    for ticks in tickers:
        returns[ticks + ' return'] = bank_stocks[ticks]['Close'].pct_change()
    print('THE HEAD OF TH RETURNS DATAFRAME')
    # dropping NaN values
    returns.dropna(inplace=True)
    print(returns.head(5))
    # setting the seaborn plot style for all plots
    sns.set_style('whitegrid')



def close_high():
    '''
    using the cross section .xs function to
    print the highest single day closing value of various banks
    '''
    print( bank_stocks.xs(key='Close', axis=1, level='Stock Info').max())


'''
drawing a pairplot for the returns value of each bank against ALL other banks
'''


def draw_pair():
    sns.pairplot(data=returns, kind='reg', diag_kind='kde' )
    plt.show()


def dt_max_min():
    '''
    this part of the code is faulty.
    It is supposed to print the dataframe containing the date of worst and best single day return
    of each bank.
    I have done this instead using the idxmax() and idx min finction
    the faulty code is as follows
    ------------------------------------------------------------------------------------------------------
    ret_max=pd.Series()
    ret_min=pd.Series()
    def check_ret_max():
        for p in tickers:
            ret_max.append(returns[p+' return'].argmax())
        return ret_max()
    def check_ret_min():
        for p in tickers:
            ret_min.append(returns[p+' return'].argmin())
        return ret_min()

    check_ret_min()
    check_ret_max()

    print (ret_max)
    print (ret_min)
    ------------------------------------------------------------------------------------------------------
    '''
    print('MIN RETURNS')
    print(returns.idxmin())
    print()
    print('MAX RETURNS')
    print()
    print(returns.idxmax())


def show_std():
    # prints the standard deviation of the returns of all the banks
    print('STANDARD DEVIATION OF THE RETURNS OF THE STOCKS IS:')
    print(returns.apply(np.std))


def draw_distplot(st, en, sto):
    '''
    creating a distplot of returns of year 2015 of morgan stanley stocks
    '''
    sns.distplot(returns.loc[dt.datetime(st[0], st[1], st[2]):dt.datetime(en[0], en[1], en[2])][sto + ' return'], bins=100, color='green', kde=True)
    plt.show()


def draw_lineplot():
    '''
    creating a line plot of all the banks' closing value
    '''
    bank_stocks.xs(key='Close', level=1, axis=1).plot(figsize=(16, 9), label=tickers)
    plt.legend()
    plt.show()


def draw_heatmap():
    '''
    heatmap of correlation of closing values of all banks
    '''
    sns.heatmap(data=bank_stocks.xs(key='Close', level=1, axis=1).corr(), cmap='magma', annot=True)
    plt.show()


def draw_clustermap():
    '''
    clustermap of correlation of closing values of all banks
    '''

    sns.clustermap(bank_stocks.xs(key='Close', level=1, axis=1).corr(), cmap='magma', annot=True)
    plt.show()
    plt.tight_layout()
