#!/usr/bin/env python3
import sys
keys=[]
val_list=[]
bound=0
def StandardSN(vals,w):
 temp=[]
 temp6=[]
 arr=[]
 for i in range(0,len(vals)):
  t=vals[i].split(',')
  temp6.append(t)
  temp.append(t[3].split(';'))
 for i in range(0,len(temp)-w+1):
  for j in range(i+1,i+w):
   for str1 in temp[i]:
    if str1 in temp[j]:
     l='# '
     l+=temp6[i][1]+"\t"+temp6[j][1]
     if l not in arr:
      arr.append(l)
      print(l)


		
for i in sys.stdin:
    i=i.strip()
    key,val=i.split("\t",1)
    val_list.append(val)
    keys.append(key)
w=5#window_size
StandardSN(val_list,w)#comparisons
first=[]
last=[]
curr_key=0
for j in range(0,len(val_list)):
    if j<=w-1:
        first.append(val_list[j])
    elif j>=(len(val_list)-(w-1)):
        last.append(val_list[j])
for i in range(0,len(keys)):
    k=keys[i].split(".")
    if k[0]=='1':
     curr_key=1
    elif k[0]=='2':
     curr_key=2
    if curr_key>1:
        bound=curr_key-1
        for x in first:
            s=''
            s+=str(bound)
            s=s+"."+keys[i]
            print(s+'\t'+x)#output of 1st phase and input for secind phase
    elif curr_key<2:
        bound=curr_key
        for x in last:
            s=''
            s+=str(bound)
            s=s+"."+keys[i]
            print(s+'\t'+x)#output of 1st phase and input for secind phase
