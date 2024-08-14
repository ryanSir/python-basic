import my_info

print(my_info.name)

import my_info as a

print(a.info())

# 2 from ... import
from my_info import name

print(name)

from my_info import info

print(info())

# 通配符
from my_info import *

print(name)
print(info())

# 同时导入多个模块，如果有同名的，
import math, time, random

from my_info import *
from introduce import *

# 导入模块中出现同名的变量和函数 ,后面会覆盖前面的
info()
my_info.info()