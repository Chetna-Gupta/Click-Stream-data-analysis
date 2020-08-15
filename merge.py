import pandas as pd
import numpy as np
from pandas import DataFrame
from pandas import Series
#first run
'''
data = pd.read_csv("click_which_are_not_buys_dataware_part7.csv")
#print data


new = data[['total_time_spent_on_item', 'offer', 'hour_of_day','no_of_clicks_on_item','Holiday','day_of_week','buys_or_not','click_cat']].copy()
#print new

new.insert(8,"weekday",0)
#print new[0]
#print new[1]


d=new["day_of_week"]
#print d
leng=len(new.index)

#print leng


for i in range(0,leng):
    x=str(d[i])
    if (x=="Monday"):
        new.set_value(i,"weekday",0)
    elif (x=="Tuesday"):
        new.set_value(i,"weekday",1)
    elif (x=="Wednesday"):
        new.set_value(i,"weekday",2)
    elif (x=="Thursday"):
        new.set_value(i,"weekday",3)
    elif (x=="Friday"):
        new.set_value(i,"weekday",4)
    elif (x=="Saturday"):
        new.set_value(i,"weekday",5)
    else:
        new.set_value(i,"weekday",6)



#print new
new.to_csv("part1.csv",index=False)

'''





#second run

dta = pd.read_csv("part1.csv")
#print data

dta=dta.drop('day_of_week',axis=1)
dta.insert(8,"total_time_taken_to_buy",0)
#print dta
#dta.to_csv("merge_part1.csv",index=False)
dta.to_csv("merge_part7.csv",index=False)


dta2 = pd.read_csv("clicks_which_are_buys_dw(c).csv")
#print dta2

new1 = dta2[['total_time_spent_on_item','offer', 'hour_of_day','no_of_clicks_on_item','Holiday','buys_or_not','click_cat','weekday','total_time_taken_to_buy']].copy()
#print new1

#new1.insert(0,'total_time_spent_on_item',0)
#print new1


with open('merge_part7.csv', 'a') as f:
    new1.to_csv(f, header=False,index=False)





'''

#third run

dt = pd.read_csv("merge_part1.csv")
print dt
'''

