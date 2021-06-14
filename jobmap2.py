#!/usr/bin/env python3
import sys
for i in sys.stdin:
 i=i.strip()
 key,val=i.split("\t",1)
 print('{0}\t{1}'.format(key,val))
