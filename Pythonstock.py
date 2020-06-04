import pandas as pd
import numpy as np
import yfinance as yf
import datetime as dt
from pandas_datareader import data as pdr



yf.pdr_override()

stock=input("Enter a stock ticker symbol: ")
print(stock)

startyear = 2019
startmonth= 1
startday= 10

#date time object


start=dt.datetime(startyear,startmonth,startday)

now=dt.datetime.now()

df=pdr.get_data_yahoo(stock,start,now)


#moving average 50 day

ma=50
smaString="Sma_"+str(ma)

#create moving average column simplie movinng average in pandas

df[smaString]=df.iloc[:,4].rolling(window=ma).mean()



df=df.iloc[ma:]

numH=0
numC=0

for i in df.index:
    print(df["Adj Close"][i])

    #moving average and adjusted close
if(df["Adj Close"][i]>df[smaString][i]):
    print("The close high")
    numH+=1
else:
    print("close lower")
    numC+=1
print(str(numH))
print (str(numC))
