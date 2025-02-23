import math
import os
import random
import re
import sys

def solve(s):
    #指定' '為分隔符號，保留多個空格
    return ' '.join([w.capitalize() for w in s.split(' ')])
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
