import admin.my_admin as a

a.info()

from admin import my_admin as b

b.info()

from admin.my_admin import info

info()

from admin.my_admin import *
info()
