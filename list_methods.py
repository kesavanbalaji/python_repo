# Append:
# -------

# a=[10,20,30,'apple']
# a.append(40)
# a
# [10, 20, 30, 'apple', 40]
# a.append('hi')
# [10, 20, 30, 'apple', 40, 'hi']
#  for i in range(10):
# ...     b=input()
# ...     a.append(b)
# ...
# 10
# 20
# 30
# 40
# 50
# 60
# 70
# 80
# 90
# 100
#  a
# [10, 20, 30, 'apple', 40, 'hi', '10', '20', '30', '40', '50', '60', '70', '80', '90', '100']

# clear()
# -------
# a.clear()
# a
# []

# copy()
# b=a.copy()
# b
# [10, 20, 30, [40, 50], 60]
# a
# [10, 20, 30, [40, 50], 60]
# a[-2][1]=100
# a
# [10, 20, 30, [40, 100], 60]
# b
# [10, 20, 30, [40, 100], 60]

# count()
# -------
# a.count(10)
# 1
# a.append(10)
# a
# [10, 20, 30, [40, 100], 60, 10]
# a.count(10)
# 2
# extend()
# --------
# a.extend('hi')
# a
# [10, 20, 30, [40, 100], 60, 10, 'h', 'i']
# a.extend(10)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: 'int' object is not iterable
# a.extend([10])
# a
# [10, 20, 30, [40, 100], 60, 10, 'h', 'i', 10]
