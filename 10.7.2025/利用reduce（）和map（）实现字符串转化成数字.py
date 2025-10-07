
from functools import reduce

def str2float(s):
    def fn(x, y):
        return x * 10 + y
    def char2num(s):
        digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
        return digits[s]
    dot_index = s.find('.')
    xiaoshugeshu = len(s)-1-dot_index
    b = s.replace(".",'')
    return reduce(fn,map(char2num,b))/10**xiaoshugeshu
str2float('123.456')
print(str2float('123.456'))
print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')







a = '123.456'
print(a[0])
# for i in range(len(a)):
#     while a[i] == '.':
#         break
# xiaoshugeshu = len(a)-1-i
dot_index = a.find('.')
xiaoshugeshu = len(a)-1-dot_index
b = a.replace(".",'')
print(b)


    