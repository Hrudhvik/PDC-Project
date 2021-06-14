#!/usr/bin/env python3
import sys
def partition_prefix(key):
	partition_key=""
	arr1=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M']
	arr2=[ 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
	if key[0] in arr1:
		partition_key+='1'
	if key[0] in arr2:
		partition_key+='2'
	return partition_key
for i in sys.stdin:
	i=i.strip()
	entity=i.split(",")
	year=entity[5]
	author=entity[3].split(";")
	key=""
	for j in author:
		k=j.strip()
		k=k.split(" ") #first letters of author's last name
		key=key+k[0]
	mod_key=key+"-"+str(year)
	temp_key=partition_prefix(mod_key)+"."+mod_key
	value=i
	print('{0}\t{1}'.format(temp_key,value))
