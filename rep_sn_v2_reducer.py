#!/usr/bin/env python3
import sys


def StandardSN(vals, w):
    temp = []
    temp6 = []
    arr = []
    for i in range(0, len(vals)):
        t = vals[i].split(',')
        temp6.append(t)
        temp.append(t[3].split(';'))
    for i in range(0, len(temp)-w+1):
        for j in range(i+1, i+w):
            for str1 in temp[i]:
                if str1 in temp[j]:
                    l = '# '
                    l += temp6[i][1]+"\t"+temp6[j][1]
                    if l not in arr:
                        arr.append(l)
                        print(l)


no_of_partitions = 2
window_size = 5
keys_partition1 = []
keys_partition2 = []
keys_rep_sn = []
val_list_partition_1 = []
val_list_partition_2 = []
val_rep_sn = []
bound = 1

for i in sys.stdin:
    i = i.strip()
    if (i[0] == '*'):
        continue
    key, val = i.split("\t", 1)
    if (key[0] == '1'):
        val_list_partition_1.append(val)
        keys_partition1.append(key)
    elif (key[0] == '2'):
        if (key[2] == '2'):
            val_list_partition_2.append(val)
            keys_partition2.append(key)
        elif (key[2] == '1'):
            val_rep_sn.append(val)
            keys_rep_sn.append(key)

w = 5  # window_size
combined_partition = val_rep_sn + val_list_partition_2
# for i in sorted(keys_partition1):
#     print(i, val_list_partition_1[keys_partition1.index(i)])
# sorted_1 = [x for _, x in sorted(zip(keys_partition1, val_list_partition_1))]
# for i in sorted(sorted_1):
#     print(i)
# print('*****')

# print(sorted(combined_partition))
StandardSN((val_list_partition_1), w)  # comparisons
StandardSN(combined_partition[len(val_rep_sn)+1-w:], w)
first = []
last = []
curr_key = 0
