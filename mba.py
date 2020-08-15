#import unittest
from pymining import itemmining, perftesting, assocrules
import csv
import pandas as pd
import numpy as np
#first run
'''
with open('mba_data.csv') as f:
    transactions=[tuple(line) for line in csv.reader(f)]


#transactions = perftesting.get_default_transactions()
#print type(transactions)
#print transactions
relim_input = itemmining.get_relim_input(transactions)
item_sets = itemmining.relim(relim_input, min_support=2)
#rules = assocrules.mine_assoc_rules(item_sets, min_support=10, min_confidence=0.8)
rules = assocrules.mine_assoc_rules(item_sets, min_support=5, min_confidence=0.7)
f= open("frequentset_data.csv","w+")
a=""
for r in item_sets:
    print r
    c=0
    for re in r:
        print re
        re=str(re)
        if c==0:
            a=re
        else:
            a = a + "," + re
        c=c+1
    f.write(a + "\n")
    a=""

f.close()
'''

df=pd.read_csv("final_predictions_only_buys_part1.csv")
#f= open("final_predictions_only_buys_part1(mba).csv","w")
#df1=pd.read_csv("frequentset_data.csv")
wr=""
arr=[]
iid=df['click_iid']
hj=len(df)
for i in range(0,10):
    a=str(iid[i])
    wr=a
    with open('frequentset_data.csv', 'rt') as f:
        reader = csv.reader(f, delimiter=',')
        for row in reader:
            for field in row:
                if field == a:
                    #print "is in file"
                    print row


                    arr.append(row)
        print "end"

'''
for i in range(0,10):
  print arr
  print arr[i]
'''
'''
   for j in range(0,5):
     print arr[0][j]
'''

'''
                    for field in row:
                         if a!=field:
                          wr= wr +','+ field
                          #df[i,'recommende_item']=field+','
                          print wr



                wr=""'''



#print df
#df.to_csv("final_predictions_only_buys_part1(mba).csv",index=False)



'''
print rules
'''

'''
for yo in rules:
    print yo
    print yo[0]
    print yo[1]

'''


'''
print type(rules)
print rules[0]
print type(rules[0])
print rules[0][0]
print type(rules[0][0])
#print rules[0][0][0]
'''