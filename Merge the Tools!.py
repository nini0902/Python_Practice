from itertools import groupby
import textwrap
def merge_the_tools(string, k):
    substring = textwrap.wrap(string, k)
    
    merged = []
    for sub in substring:
        seen = set()
        merge_sub = ''.join(ch for ch in sub if ch not in seen and not seen.add(ch))
        merged.append(merge_sub)
    
    for i in merged: print(i)

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
