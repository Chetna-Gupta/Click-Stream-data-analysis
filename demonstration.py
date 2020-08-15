import pandas as pd
import numpy as np

#df=pd.read_csv("test_dataware_part1.csv")
df1=pd.read_csv("test_final_dw_part1.csv")
df2=pd.read_csv("final_predictions_with_iids.csv")
df3=pd.read_csv("recommended_items_final.csv")

for i in range(0,10):
    print 'the session id is ' , df2.loc[i,'click_sid'],'\t the item id is ',df2.loc[i,'click_iid'],'\n'
    print 'the total time spent on item is ',df1.loc[i,'total_time_spent_on_item'],'the hour of the day is ',df1.loc[i,'hour_of_day'],'\n'
    if df1.loc[i,'Holiday']==0:
        print 'there is no holiday\t'
    else:
        print 'there is a holiday\t'

    if df1.loc[i, 'offer'] == 0:
        print 'there is no offer\n'
    else:
        print 'there is a offer\n'

    if df2.loc[i,'final_prediction']==1:
        print 'the prediction is user will buy\n'
        if i==8:
         print 'the other recommended items are ',df3.loc[0,"recommended item1"],df3.loc[0,"recommended item2"],df3.loc[0,"recommended item3"]
        elif i == 9:
          print 'the other recommended items are ', df3.loc[1, "recommended item1"], df3.loc[1, "recommended item2"],df3.loc[1, "recommended item3"]
        elif i==10:
         print 'the other recommended items are ',df3.loc[2,"recommended item1"],df3.loc[2,"recommended item2"],df3.loc[2,"recommended item3"]

    else:
        print 'the user will not buy'

