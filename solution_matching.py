import pandas as pd
import numpy as np
#first run
'''
column_names=['a','b','c','d','e','f','g','h','i','j','k']
df=pd.read_csv("C:\Users\Chetna\Desktop\yoochoose-dataFull\solution.csv",header=None,low_memory=False,names=column_names)
df["a"]=df['a'].astype(str)
print df['a'].str.split(';',expand=True)
gh=df['a'].str.split(';',expand=True)
#print "end"
#print df['b']
#print "end2"
#print df['c']
#print "end3"
print gh
print "end4"

print df
gh[0]=gh[0].astype(int)
gh[1]=gh[1].astype(int)
print gh
gh.to_csv("solution2.csv",index=False)
'''

#second run
'''
df1=pd.read_csv("solution2.csv")
column_names=['a','b','c','d','e','f','g','h','i','j','k']
df=pd.read_csv("C:\Users\Chetna\Desktop\yoochoose-dataFull\solution.csv",header=None,low_memory=False,names=column_names)
df1[2]=df['b']
df1[3]=df['c']
df1[4]=df['d']
df1[5]=df['e']
df1[6]=df['f']
df1[7]=df['g']
df1[8]=df['h']
df1[9]=df['i']
df1[10]=df['j']
df1[11]=df['k']
print df1
df1.to_csv("solution2.csv",index=False)
'''

#third run

'''
df1=pd.read_csv("solution2.csv")
df=pd.read_csv("final_predictions_only_buys_part1.csv")
legn=len(df1)
l1=len(df)
a=df1.iloc[:,0]
b=df1.iloc[:,1]
c=df1.iloc[:,2]
d=df1.iloc[:,3]
e=df1.iloc[:,4]
f=df1.iloc[:,5]
g=df1.iloc[:,6]
h=df1.iloc[:,7]
i1=df1.iloc[:,8]
jk=df1.iloc[:,9]
k=df1.iloc[:,10]
l=df1.iloc[:,11]

df['click_sid']=df['click_sid'].astype(int)
df['click_iid']=df['click_iid'].astype(int)

sid=df['click_sid']
iid=df['click_iid']
iv=[]

if sid[0]==15:
 print sid[0]
j=0

for i in range (0,200):
    #iv.append(9)
    if a[i]<=6464520:
        #print a[i]
        for j in range(0,l1):
         if a[i]==sid[j]:
            print a[i]
            if b[i]==iid[j]:
                iv.append(1)
                print "end3"
            elif c[i]==iid[j]:
                iv.append(1)
            elif d[i]==iid[j]:
                iv.append(1)
            elif e[i]==iid[j]:
                iv.append(1)
            elif f[i]==iid[j]:
                iv.append(1)
            elif g[i]==iid[j]:
                iv.append(1)
            elif h[i]==iid[j]:
                iv.append(1)
            elif i1[i]==iid[j]:
                iv.append(1)
            elif jk[i]==iid[j]:
                iv.append(1)
            elif k[i]==iid[j]:
                iv.append(1)
            elif l[i]==iid[j]:
                iv.append(1)
            else:
                iv.append(0)
         else:
            continue

    else:
        continue
print iv
df3=pd.DataFrame({'right_wrong':iv[:]})
df3.to_csv("soln_match.csv",index=False)
#print df1.iloc[0,0]
#print df1
#print df
'''
#last run

df=pd.read_csv("soln_match.csv")
check=df['right_wrong']
k=len(check)
rcount=0
for i in range(0,k):
    print check[i]
    if check[i]==1:
        print "yes"
        rcount=rcount+1

print rcount
print k
accuracy=(float(rcount)/float(450))*100
print "accuracy="
print accuracy
