import pandas as pd
import numpy as np


#first run
'''
df=pd.read_csv("predict_try2_1.csv")
new=df[['predict1']].copy()

print new
new.to_csv("final_predict_all_cases_part2.csv",index=False)
'''

#second run
'''

df2=pd.read_csv("predict_try2_2.csv")
df3=pd.read_csv("predict_try2_3.csv")
df4=pd.read_csv("predict_try2_4.csv")
df5=pd.read_csv("predict_try2_5.csv")
df6=pd.read_csv("predict_try2_6.csv")
df7=pd.read_csv("predict_try2_7.csv")
gh=pd.read_csv("final_predict_all_cases_part2.csv")
print gh
gh['predict2']=df2[['predict2']]
gh['predict3']=df3[['predict3']]
gh['predict4']=df4[['predict4']]
gh['predict5']=df5[['predict5']]
gh['predict6']=df6[['predict6']]
gh['predict7']=df7[['predict7']]

print gh
gh.to_csv("final_predict_all_cases_part2.csv",index=False)
'''

#third run

gh=pd.read_csv("final_predict_all_cases_part2.csv")
print gh

gh['mean']=gh.mean(axis=1)
print gh
gh["final_predict"]= np.where(gh['mean']<=0.571429,0,1)
print gh
gh.to_csv("final_predict_all_cases_part2.csv",index=False)
