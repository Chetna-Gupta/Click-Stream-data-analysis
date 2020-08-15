import pandas as pd
import numpy as np
from pandas import DataFrame
from pandas import Series
#first run

#data = pd.read_csv("test_dataware_part1.csv")
data = pd.read_csv("test_dataware_part2.csv")
#print data


new = data[['total_time_spent_on_item', 'offer', 'hour_of_day','no_of_clicks_on_item','Holiday','weekday','click_cat']].copy()
#print new


#print new[0]
#print new[1]





print new
#new.to_csv("test_final_dw_part1.csv",index=False)
new.to_csv("test_final_dw_part2.csv",index=False)

