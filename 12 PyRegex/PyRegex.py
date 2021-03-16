import re

res = re.match(r'\d+qwq$', '1428717646qwq')

a = 'a  b c , d, e ,,, f ;          g'
print(re.split(' ', str(a)))
print(re.split(r'\s+', str(a)))
print(re.split(r'[\s\,\;]+', str(a)))

m = re.match(r'^(\d{3})-(\d{3,8})$', '010-12345')
print(m.group(0) + ' ~ ' + m.group(1) + ' ~ ' + m.group(2))

# 正则表达式默认是贪婪匹配，会匹配尽可能多的字符
print(re.match(r'^(\d+)(0*)$', '102300').groups())
# 添加 '?' 将其设置为非贪婪匹配
print(re.match(r'^(\d+?)(0*)$', '102300').groups())