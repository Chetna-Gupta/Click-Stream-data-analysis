from __future__ import print_function
import pandas as pd
import numpy as np
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier, export_graphviz
import pydotplus


#df = pd.read_csv("merge_part1.csv")
#df = pd.read_csv("merge_part2.csv")
#df = pd.read_csv("merge_part3.csv")
#df = pd.read_csv("merge_part4.csv")
#df = pd.read_csv("merge_part5.csv")
#df = pd.read_csv("merge_part6.csv")
df = pd.read_csv("merge_part7.csv")



print(df)

target = df["buys_or_not"]
features = df[list(df.iloc[:,0:5]) + list(df.iloc[:,6:8])]
print("* features:", features, sep="\n")


y = target #target
X = features
dt = DecisionTreeClassifier(min_samples_split=20, random_state=99)
dt=dt.fit(X, y)

with open("merge_part2_7.dot", 'w') as f:                                     #change the name accordingly
     f = tree.export_graphviz(dt, out_file=f)


'''
dot_data = tree.export_graphviz(dt, out_file=None)
graph = pydotplus.graph_from_dot_data(dot_data)
graph.write_pdf("merge_part1.pdf")
'''

#predict

#df2=pd.read_csv("test_final_dw_part1.csv")
df2=pd.read_csv("test_final_dw_part2.csv")

featuresp = df2[list(df2.iloc[:,0:])]
print (featuresp)
go=dt.predict(featuresp)
print(go)

#df3=pd.DataFrame({'predict1':go[:]})
#df3=pd.DataFrame({'predict2':go[:]})
#df3=pd.DataFrame({'predict3':go[:]})
#df3=pd.DataFrame({'predict4':go[:]})
#df3=pd.DataFrame({'predict5':go[:]})
#df3=pd.DataFrame({'predict6':go[:]})
df3=pd.DataFrame({'predict7':go[:]})

#df3.to_csv("predict_try2_1.csv")
#df3.to_csv("predict_try2_2.csv")
#df3.to_csv("predict_try2_3.csv")
#df3.to_csv("predict_try2_4.csv")
#df3.to_csv("predict_try2_5.csv")
#df3.to_csv("predict_try2_6.csv")
df3.to_csv("predict_try2_7.csv")

