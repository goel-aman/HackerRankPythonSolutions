#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    output = ""
    i = 0
    output += s[0].upper()
    for i in range(1,len(s)):
        if(s[i-1] == ' '):
            output += s[i].upper()
            continue
        else:
            output += s[i]
    return output

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
