import numpy as np
import pandas as pd
from pandas import DataFrame
from pandas import Series
from pandas.tseries.holiday import USFederalHolidayCalendar as calendar



f= open("mba_data.csv","w+")
#df = pd.read_csv("clicks_part1.csv")

#f=open("mba_data.csv", "a")
#df = pd.read_csv("clicks_part3.csv")

column_names=['buys_sid','buys_time','buys_iid','buys_price','buys_qun']
df = pd.read_csv("E:\Desktop_Data\major\yoochoose-buys.csv",low_memory=False,header= None,names= column_names)
#print data
df.sort_values(by='buys_sid', ascending=1)


g= df["buys_sid"]
h= df["buys_iid"]
leng=len(df.index)
#df.insert(9,"time_spent_on_item_1",0)
a=""
for i in range(0,leng):
    if(i==0):
        x=str(g[i])
        m=str(h[i])
        a=m
    else:
        y=str(g[i])
        m=str(h[i])
        if(x==y):
            a=a+","+m
        else:
            f.write(a+"\n")
            x=y
            a=""
            a=m
        x=y




f.close()



'''
f=open("mba_data.csv", "r")
if f.mode == 'r':
    contents =f.read()
print contents
'''
'''
with open('mba_data.csv') as f:
    print sum(1 for _ in f)
'''