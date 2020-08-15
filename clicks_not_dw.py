import numpy as np
import pandas as pd
from pandas import DataFrame
from pandas import Series
from pandas.tseries.holiday import USFederalHolidayCalendar as calendar

def explore_time(ts):
    day= ts.days
    sec=ts.seconds
    if day >= 0:
        total= sec
    else:
        total=0
    return total

def hr_func(ts):
    return ts.hour


#df = pd.read_csv("click_which_are_not_buys_part1.csv")
#df = pd.read_csv("click_which_are_not_buys_part2.csv")
#df = pd.read_csv("click_which_are_not_buys_part3.csv")
#df = pd.read_csv("click_which_are_not_buys_part4.csv")
#df = pd.read_csv("click_which_are_not_buys_part5.csv",low_memory=False)
#df = pd.read_csv("click_which_are_not_buys_part6.csv")
df = pd.read_csv("click_which_are_not_buys_part7.csv")


df["click_time"]=pd.to_datetime(df["click_time"])
df["day_of_week"] = df["click_time"].dt.weekday_name
#print df


dr = pd.date_range(start='2014-01-01', end='2014-12-31')

cal = calendar()
holidays = cal.holidays(start=dr.min(), end=dr.max())

df["Holiday"] = df["click_time"].isin(holidays)
#print df

print len(df)
'''
for i in range (0,len(df)-1):
    j=i+1
    #print df
    if i==0:
        #print df.loc[i,'a']
        #print df.loc[i,'b']
        df.loc[i,'time_spent_on_item']=df.loc[i+1,'click_time']-df.loc[i,'click_time']
        #df["difference_time"] = df['b'].shift(-1) - df['b']
        #print df.loc[i,'difference_time']
        #print df

    elif df.loc[i,'click_sid']== df.loc[i-1,'click_sid'] and df.loc[i,'click_sid']==df.loc[i+1,'click_sid'] :
     #print df.loc[i,'a']
     #print df.loc[i,'b']
     df.loc[i, 'time_spent_on_item'] = df.loc[i + 1, 'click_time'] - df.loc[i, 'click_time']
     #df["difference_time"] = df['b'].shift(-1)-df['b']
     #print df.loc[i,'difference_time']
    elif df.loc[i,'click_sid']!= df.loc[i-1,'click_sid'] and df.loc[i,'click_sid']== df.loc[i+1,'click_sid']:
        df.loc[i, 'time_spent_on_item'] = df.loc[i + 1, 'click_time'] - df.loc[i, 'click_time']

    elif df.loc[i,'click_sid']!=df.loc[i+1,'click_sid']:
        #print df.loc[i,'a']
        #print df.loc[i,'b']
        df.loc[i, 'time_spent_on_item'] = 0
        #df["difference_time"]= "NaT"
        #print df.loc[i,'difference_time']
'''
df['time_spent_on_item']=df['click_time'].shift(-1)-df['click_time']
#df['time_spent_on_item']=np.where(df['time_spent_on_item']<0,0,df['click_time'].shift(-1)-df['click_time'])
df.loc[len(df)-1,'time_spent_on_item'] = df.loc[1,'click_time']-df.loc[0,'click_time']
df["total_time_spent_on_item"]=df["time_spent_on_item"].apply(explore_time)



print df

df["hour_of_day"]=df['click_time'].apply(hr_func)
df['no_of_clicks_on_item']=df.groupby('click_iid')['click_iid'].transform('count')
df['click_cat']=df['click_cat'].astype(str)
df["offer"]= np.where(df['click_cat']=='S',1,0)
print df

#df.to_csv("click_which_are_not_buys_dataware_part1.csv",index=False)
#df.to_csv("click_which_are_not_buys_dataware_part2.csv",index=False)
#df.to_csv("click_which_are_not_buys_dataware_part3.csv",index=False)
#df.to_csv("click_which_are_not_buys_dataware_part4.csv",index=False)
#df.to_csv("click_which_are_not_buys_dataware_part5.csv",index=False)
#df.to_csv("click_which_are_not_buys_dataware_part6.csv",index=False)
df.to_csv("click_which_are_not_buys_dataware_part7.csv",index=False)


