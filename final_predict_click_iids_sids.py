import pandas as pd
import numpy as np

#first run
'''
#df=pd.read_csv("test_part1.csv")
df=pd.read_csv("test_part2.csv")

new=df[['click_sid','click_iid']].copy()
print new
#new.to_csv("final_predictions_with_iids.csv",index=False)
new.to_csv("final_predictions_with_iids2.csv",index=False)
'''
#second run
'''
#df=pd.read_csv("final_predictions_with_iids.csv")
df=pd.read_csv("final_predictions_with_iids2.csv")

#df2=pd.read_csv("final_predict_all_cases_part1.csv")
df2=pd.read_csv("final_predict_all_cases_part2.csv")

df['final_prediction']=df2['final_predict']
print df
#df.to_csv("final_predictions_with_iids.csv",index=False)
df.to_csv("final_predictions_with_iids2.csv",index=False)
'''
#third run

#df=pd.read_csv("final_predictions_with_iids.csv")
df=pd.read_csv("final_predictions_with_iids2.csv")

cond=df.ix[(df['final_prediction']==1)]
print cond
#cond.to_csv("final_predictions_only_buys_part1.csv")
cond.to_csv("final_predictions_only_buys_part2.csv")
