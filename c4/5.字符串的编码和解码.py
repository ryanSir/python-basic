s = '你好'

# 编码 str -> bytes
s_code = s.encode(errors='replace')  # 默认是utf-8,中文占3个字节
print(s_code)

s_code_gbk = s.encode('gbk', errors='replace')  # 中文占两个字节
print(s_code_gbk)

# errors: ignore/replace/strict

# 解码
print(bytes.decode(s_code, 'utf-8'))
print(bytes.decode(s_code_gbk,'gbk'))
