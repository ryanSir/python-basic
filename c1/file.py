fp = open('note.txt', 'w')  # 打开文件,如果当前路径下没有会新建 w-->write
print('hello word', file=fp)  # 写入文件
fp.close()  # 关闭文件
