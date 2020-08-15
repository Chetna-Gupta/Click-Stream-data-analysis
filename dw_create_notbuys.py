import pandas as pd

data = pd.read_csv("clicks_part1.csv")
# data = pd.read_csv("clicks_part2.csv")
# data = pd.read_csv("clicks_part3.csv")
# data = pd.read_csv("clicks_part4.csv",low_memory=False)
# data = pd.read_csv("clicks_part5.csv",low_memory=False)
# data = pd.read_csv("clicks_part6.csv",low_memory=False)
#data = pd.read_csv("clicks_part7.csv",low_memory=False)
print data

dt = pd.read_csv("common.csv")
#print dt

#x=dt["click_sid"]==11
#print x

merged = data.merge(dt, how='left', indicator=True,left_on=['click_sid', 'click_iid'], right_on=['click_sid', 'click_iid'])
print merged

merger1=merged[merged['_merge']=='left_only']
print merger1

m=merger1.filter(['click_sid','click_time','click_iid','click_cat'],axis=1)
print m

m.insert(4,"buys_or_not",0)
print m

#m.to_csv("click_which_are_not_buys_part1.csv",index=False)
#m.to_csv("click_which_are_not_buys_part2.csv",index=False)
#m.to_csv("click_which_are_not_buys_part3.csv",index=False)
#m.to_csv("click_which_are_not_buys_part4.csv",index=False)
#m.to_csv("click_which_are_not_buys_part5.csv",index=False)
#m.to_csv("click_which_are_not_buys_part6.csv",index=False)
m.to_csv("click_which_are_not_buys_part7.csv",index=False)