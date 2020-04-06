#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict
# Complete the checkMagazine function below.


def checkMagazine(magazine, note):
    dicty = defaultdict(int)
    for word in magazine:
        dicty[word]+=1
    for word in note: 
        if dicty[word]==0 : print("False") 
        dicty[word]-=1
    print("True")         
  



if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)
