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
 if i[0]!='#':
    i=i.strip()
    key,val=i.split("\t",1)
    val_list.append(val)
    keys.append(key)
 elif i[0]=='#':
  print(i)
w=5#window_size
StandardSN(val_list,w)#comparisons
