from calculator import *

s = "|-5-\u221a225|"
# s = "(-3-(1+2))"
# res = TextFormatter.format(s)
res = Calculator().calc(s)
print(res)