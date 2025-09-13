
s = map(chr,input().split())
#print(' '.join(f"{ord(c):02X}" for c in s))

# 方法1: 转换为列表打印
print(list(s))

# 方法2: 如果要重新使用map对象，需要重新创建
# s = map(chr,input().split())
# print(''.join(s))
