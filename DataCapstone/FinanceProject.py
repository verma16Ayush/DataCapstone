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

'''
creating a list object ticker and storing a list of all the tickers of the bank
in alphabetical order 
'''
tickers = ('BAC C GS MS JPM WFC'.split())
tickers.sort()
print(tickers)

# create a new dataframe merging all the data of the banks
bank_stocks = pd.concat([bac, c, gs, jpm, ms, wfc], axis=1, keys=tickers)

# printing the head of the bank stocks dataframe
print(bank_stocks.head())

# naming the two levels of columns
bank_stocks.columns.names = ['Bank Ticker', 'Stock Info']

# print the dataframe head again with new column indices
print(bank_stocks.head(2))

'''
using the cross section .xs function to
print the highest single day closing value of various banks
'''
print(bank_stocks.xs(key='Close', axis=1, level='Stock Info').max())

'''
creating a new dataframe returns and storing the percentage change values of 
of closing values of all the bAnks
printing the head of the returns dataframe
'''
returns = pd.DataFrame()
for ticks in tickers:
    returns[ticks + ' return'] = bank_stocks[ticks]['Close'].pct_change()

print(returns.head(5))
# dropping NaN values
returns.dropna(inplace=True)

'''
setting the seaborn plot style for all 
plots and draawing a pairplot for the returns value of each bank against ALL other banks
'''
sns.set_style('whitegrid')
sns.pairplot(data=returns, kind='reg', diag_kind='kde', )
plt.show()

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
print(returns.idxmin())
print(returns.idxmax())

#prints the standard deviation of the returns of all the banks
print('STANDARD DEVIATION OF THE BANKS IS:')
print(returns.apply(np.std))


'''
creating a distplot of returns of year 2015 of morgan stanley stocks 
'''
sns.distplot(returns.loc[dt.datetime(2015,1,1):dt.datetime(2015,12,31)]['MS return'],bins=100,color='green',kde=True)
plt.show()

'''
creatng the distplot of citibank return of year 2008
'''
sns.distplot(returns.loc[dt.datetime(2008,1,1):dt.datetime(2008,12,31)]['C return'],bins=100,color='red')
plt.show()

'''
creating a line plot of all the banks' closing value
'''
bank_stocks.xs(key='Close',level=1,axis=1).plot(figsize=(16,9),label=ticks)
plt.legend()
plt.show()

'''
heatmap of correlation of closing values of all banks
'''
sns.heatmap(bank_stocks.xs(key='Close',level=1,axis=1).corr(),cmap='magma',annot=True)
plt.show()
'''
clustermap of correlation of closing values of all banks
'''

sns.clustermap(bank_stocks.xs(key='Close',level=1,axis=1).corr(),cmap='magma',annot=True)
plt.show()
plt.tight_layout()