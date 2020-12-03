# 正则表达式：字符串模式（判断字符串是否符合一定的标准）
import re

# pat = re.compile('AA')  # 此处的AA 是正则表达式 用来去验证其他的字符串
# m = pat.search("AA")  # search字符串 被校验的内容
# print(m)  # <re.Match object; span=(0, 2), match='AA'>

# m = re.search("asd","Aasd")
# print(m)  # <re.Match object; span=(1, 4), match='asd'>

# 前面的字符串是规则，后面的字符串是被校验的表达式
print(re.findall("a","ASDaDFGAa"))  # ['a', 'a']
print(re.findall("[A-Z]","ASDaDFGAa"))  # ['A', 'S', 'D', 'D', 'F', 'G', 'A']
print(re.findall("[A-Z]+","ASDaDFGAa"))  # ['ASD', 'DFGA']

# sub
print(re.sub('a','A','abcdcasd'))  # AbcdcAsd 把所有的a替换为A 从后面的字符串

# 建议在正则表达式中，被比较的字符串前面加上r，不用担心转义字符的问题
print(r"\aabd-\'")  # \aabd-\'