import pandas as pd
import numpy as np



#first run

dt = pd.read_csv("merge_part7.csv")
print dt
#print type(str(dt["Holiday"]))
#print dt["click_cat"]

#a=np.unique(dt["click_cat"])
#print a

#dt.loc[dt['Holiday'] == False, 'Holiday'] = 0
#print dt

#dt.loc[str(dt['click_cat']) == "S", 'click_cat'] = 0
#print dt

#dt.replace(['S'], [20])
#print dt


leng=len(dt.index)
d=dt["click_cat"]

for i in range(0,leng):
    x=str(d[i])
    if (x=="S"):
        dt.set_value(i,"click_cat",29)

dt[['Holiday']] = dt[['Holiday']].astype(int)
#dt[['total_time_spent_on_item']] = dt[['total_time_spent_on_item']].astype(int)
#dt[['total_time_taken_to_buy']] = dt[['total_time_taken_to_buy']].astype(int)

'''
e=dt["Holiday"]
dt.insert(9,"holiday_int",0)
for i in range(0,leng):
    x=str(e[i])
    #print x

    if (x=="True"):
        #print "yes"
        dt.set_value(i,"holiday_int",1)
    if (x=="False"):
        #print "no"
        dt.set_value(i,"holiday_int",0)

'''
print type(dt["total_time_spent_on_item"][0])
print type(dt["total_time_taken_to_buy"][0])

print type(dt["offer"][0])
print dt

dt.to_csv("merge_part7.csv",index=False)
print dt




