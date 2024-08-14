# isdigit() 十进制的阿拉伯数字
print('123'.isdigit())  # True
print('一二三'.isdigit())  # False

# 所有字符都是数字
print('123'.isnumeric())  # True
print('一二三'.isnumeric())  # True

# 所有字符都是字母(包含中文字符)
print('hello你好'.isalpha())  # True
print('hello你好123'.isalpha())  # False
print('hello你好一二三'.isalpha())  # True

# 所以字符都是字母或数字
print('hello你好'.isalnum())  # True
print('hello你好123'.isalnum())  # True

# 判断字符的大小写
print('HelloWorld'.islower())  # False
print("helo".islower())  # True

# 首字母大写
print('Hello'.istitle())  # True
print('HelloWorld'.istitle())  # False
print('Heloworld'.istitle())  # True
print('Hello World'.istitle())  # True

# 判断是否都是空白字符
print('\t'.isspace())  # True
print(' '.isspace())  # True
print('\n'.isspace())  # True
