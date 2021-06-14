#!/usr/bin/env python3
import sys
import re


def partition_prefix(key):
    partition_key = ""
    arr1 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M']
    arr2 = ['N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    if key[0] in arr1:
        partition_key += '1'
    if key[0] in arr2:
        partition_key += '2'
    # if key[0] in arr3:
    #     partition_key += '3'
    # if key[0] in arr4:
    #     partition_key += '4'
    return str(partition_key)


def map_configure(np, ws):
    # creating an empty list to store the entities with the w-1 highest blocking keys for each partition i < r
    # dimensions of x = (np-1 * ws-1)
    x = [[None for _ in range(ws - 1)]
         for _ in range(np - 1)]
    return x


def get_minimum_key(list_of_keys):
    min_key = list_of_keys[0]
    # sample key in list_of_keys = 1.AndrewJim-1900
    for key in list_of_keys:
        min_key_split = re.split('[.]', min_key)
        key_split = re.split('[.]', key)
        if (min(min_key_split[1].upper(), key_split[1].upper()) == key_split[1].upper()):
            min_key = key
    return min_key, list_of_keys.index(min_key)


def generate_blocking_key(value):
    arr = ['"', '&', '#']
    value = value.strip()
    entity = value.split(",")
    year = entity[5]
    author = []
    if (len(entity[3]) <= 1):
        author = list("Anonymous")
    else:
        author = entity[3].split(';')
    key = ""
    for j in author:
        k = j.strip()
        if k[0] in arr:
            # print("quote mark being printed")
            k = k[1:]
        elif k[-1] == '"':
            # print("quote mark being printed")
            k = k[:len(k)-1]
        k = k.split(" ")
        # concatenation of authors' first names
        key = key+k[0]
        if key[0].islower():
            # print("wah wah")
            key = key.upper()
    author = [None]
    mod_key = key+"-"+str(year)
    temp_key = partition_prefix(mod_key)+"."+mod_key
    # print("mod_key: " + mod_key + "\ntemp_key: " + temp_key)
    return temp_key


def map(value):
    entity = value
    # key is the blocking key of entity generated with format "<partiton_prefix>.<author_first_names>-<year_of_publication>"
    key = generate_blocking_key(entity)
    # the reducer assigned is the same as the partition_prefix
    parts = key.split(".")
    reducer = int(parts[0])
    bound = reducer
    if reducer < no_of_partitions:
        # indices_None is a list of indices at which None is present
        indices_None = [i for i, val in enumerate(
            rep[reducer - 1]) if val is None]
        # print(indices_None)
        # first condition is to check if correponding list for each partition contains any None
        if (len(indices_None) > 0):
            rep[reducer - 1][indices_None[0]] = entity
            keys_of_rep[reducer - 1][indices_None[0]] = key
        else:
            min_key, min_key_index = get_minimum_key(keys_of_rep[reducer - 1])
            # min_entity = rep[reducer - 1][min_key_index]
            if (key.upper() > min_key.upper() and entity not in rep[reducer - 1]):
                rep[reducer - 1][min_key_index] = entity
                keys_of_rep[reducer - 1][min_key_index] = key
    # composite key to partition by bound
    new_key = str(bound) + "." + str(key)
    return new_key, entity


no_of_partitions = 2
window_size = 5
rep = map_configure(no_of_partitions, window_size)
keys_of_rep = map_configure(no_of_partitions, window_size)


for value in sys.stdin:
    print('{0}\t{1}'.format(map(value)[0], map(value)[1]), end='')
print("************************************************")
for partition in rep:
    for i in partition:
        key = generate_blocking_key(i)
        bound = int(key[0]) + 1
        new_key = str(bound) + "." + key + "\0"
        print('{0}\t{1}'.format(new_key, i), end='')
# 167
