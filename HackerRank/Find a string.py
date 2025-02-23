import re
string = input()
sub_string = input()

#f"(?={})" 用來檢查這個字串{}所有起始位置
#主要作用是要免除忽略重疊的子字串
count = len(re.findall(f"(?={sub_string})", string))
print(count)
