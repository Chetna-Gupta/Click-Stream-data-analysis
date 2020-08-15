import pandas as pd

filename="C:\Users\Chetna\Desktop\yoochoose-dataFull\datatest.csv"
column_names_click=['click_sid','click_time','click_iid','click_cat']

#df=pd.read_csv(filename,low_memory=False,header= None,names= column_names_click,nrows=4714849)
#print df
#df.to_csv("test_part1.csv",index=False)


df1=pd.read_csv(filename,low_memory=False,header= None,names= column_names_click,skiprows=4714849,nrows=4714849)
print df1
df1.to_csv("test_part2.csv",index=False)


