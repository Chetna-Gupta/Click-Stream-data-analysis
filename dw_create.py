import pandas as pd
from pandas.tseries.holiday import USFederalHolidayCalendar as calendar
import numpy as np

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


column_names_buys= ['buys_sid','buys_time','buys_iid','buys_price','buys_qun']
loc= r'C:\Users\Chetna\Desktop\yoochoose-dataFull\buys.csv'
data = pd.read_csv(loc,low_memory=False,header= None,names= column_names_buys)
#print data




'''
filename="E:\Desktop_Data\major\yoochoose-clicks.csv"
column_names_click=['click_sid','click_time','click_iid','click_cat']
data = pd.read_csv("E:\Desktop_Data\major\yoochoose-clicks.csv",low_memory=False,header= None,names= column_names_click,dtype= {'click_sid':int,'click_time':object,'click_iid':int,'click_cat':object}  )
print data
'''

df=pd.DataFrame()
#print type(df)

def process(a):
    #b=1
    data1=a
    #print data1
    global df
    #print type(data1)

    res=pd.merge(data, data1, left_on=['buys_sid', 'buys_iid'], right_on=['click_sid', 'click_iid'],how='inner')
    #print res
    #df.append(res)
    df=pd.concat([df,res]).drop_duplicates().reset_index(drop=True)
    #print df

    #print a

chunksize=500000
filename=r'C:\Users\Chetna\Desktop\yoochoose-dataFull\clicks.csv'
column_names_click=['click_sid','click_time','click_iid','click_cat']
for chunk in pd.read_csv(filename,low_memory=False, chunksize=chunksize,header= None,names= column_names_click):
    process(chunk)


print "break"
print "break"
print "final df is"
print df


#print len(df)
#print len(df[0])


#print df[0]
df.insert(9,"buys_or_not",1)

#df.insert(df,"buys_or_not",1)

#df["buys_or_not"]=1

#df['buys_or_not'] = np.where(df['buys_sid']>=0, 1, 0)

print "break"
print "break"
print "final df after adding is"
print df
#print type(df["click_time"][0])
df["click_time"]=pd.to_datetime(df["click_time"])
df["buys_time"]=pd.to_datetime(df["buys_time"])
#print type(df["click_time"][0])
df["day_of_week"] = df["click_time"].dt.weekday_name
#print "with day of week"
#print df
df["weekday"] = df["click_time"].dt.weekday
print "with weekday and day of week"
print df
dr = pd.date_range(start='2014-01-01', end='2014-12-31')

cal = calendar()
holidays = cal.holidays(start=dr.min(), end=dr.max())

df["Holiday"] = df["click_time"].isin(holidays)
print "after holiday"
print df
df['time_spent_on_item']=df['click_time'].shift(-1)-df['click_time']
#df['time_spent_on_item']=np.where(df['time_spent_on_item']<0,0,df['click_time'].shift(-1)-df['click_time'])
df.loc[len(df)-1,'time_spent_on_item'] = df.loc[1,'click_time']-df.loc[0,'click_time']
df["total_time_spent_on_item"]=df["time_spent_on_item"].apply(explore_time)

df["time_taken_to_buy"]=df["buys_time"]-df["click_time"]
df["total_time_taken_to_buy"]=df["time_taken_to_buy"].apply(explore_time)
print "diff in buying"
print df
df["hour_of_day"]=df['click_time'].apply(hr_func)
df['no_of_clicks_on_item']=df.groupby('click_iid')['click_iid'].transform('count')
df['click_cat']=df['click_cat'].astype(str)
df["offer"]= np.where(df['click_cat']=='S',1,0)
print "FINAL"
print df
df.to_csv("clicks_which_are_buys_dw(c).csv",index=False)
#print len(df)