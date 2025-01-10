# ['capitalize', 'casefold', 'center', 'count', 
# 'encode', 'endswith', 'expandtabs', 'find', 'format', 
# 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 
# 'isdecimal', 'isdigit', 'isidentifier', 'islower', 
# 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 
# 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 
# 'partition', 'removeprefix', 'removesuffix', 'replace', 
# 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 
# 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 
# 'swapcase', 'title', 'translate', 'upper', 'zfill']

# upper()
# -------
# >>> a.upper()
# 'KESHAV'
# >>> a='KESHAV'

# lower()
# -------
# >>> a.lower()
# 'keshav'

# count()
# -------
# >>> a='this is keshav'
# >>> a.count('i')
# 2
# >>> a.count('i',2)
# 2
# >>> a.count('I',3)
# 1

# index()
# -------
# >>> a.index('i')
# 2
# >>> a.index('i',2)
# 2
# >>> a.index('s')
# 3
# >>> a.index('s',3,8)
# 3
# >>> a.index('s',4,8)
# 6

# swapcase()
# ----------
# >>> a='tHIS IS kESHAV'
# >>> a.swapcase()
# 'This is Keshav'

# capitalize()
# ------------
# >>> a.capitalize()
# 'This is keshav'
# >>> a='keshav'
# >>> a.capitalize()
# 'Keshav'

# title()
# -------
# >>> a.title()
# 'This Is Keshav'

# indexing[]
# ----------
# >>> a[-2]
# 'A'
# >>> a[0]
# 't'
# >>> a[1]
# 'H'

# slicing[]
# ---------
# >>> a[::1]
# 'tHIS IS kESHAV'
# >>> a[:]
# 'tHIS IS kESHAV'
# >>> a[::]
# 'tHIS IS kESHAV'
# >>> a[::-1]
# 'VAHSEk SI SIHt'
# >>> a[::-1 ]
# 'VAHSEk SI SIHt'


# len()
# -----
# >>> len(a)
# 14

# rindex()
# --------
# >>> a
# 'tHIS IS kESHAV'
# >>> a.index('I')
# 2
# >>> a.rindex('I')
# 5

# replace()
# ---------
# >>> a.replace('i','I',1)
# 'tHIS IS kESHAV'
# >>> a.replace('I','i',1)
# 'tHiS IS kESHAV'
# >>> a.replace('I','i',2)
# 'tHiS iS kESHAV'

# split()
# -------
# >>> a.split(' ',2)
# ['tHIS', 'IS', 'kESHAV']
# >>> a.split(' ',1)
# ['tHIS', 'IS kESHAV']
# >>> a.rsplit(' ',1)
# ['tHIS IS', 'kESHAV']

# join()
# ------
# >>> a.join(['hi','this','is','keshav'])
# 'hitHIS IS kESHAVthistHIS IS kESHAVistHIS IS kESHAVkeshav'
# >>> ' '.join(['hi','this','is','keshav'])
# 'hi this is keshav'

# strip()
# -------
# >>> a
# 'tHIS IS kESHAV'
# >>> a.strip('ist')
# 'HIS IS kESHAV'
# >>> a.strip('istv')
# 'HIS IS kESHAV'
# >>> a.strip('iHISV')
# 'tHIS IS kESHA'

# lstrip()
# --------
# >>> a.lstrip('iHISV')
# 'tHIS IS kESHAV'
# >>> a.lstrip('iHtISV')
# ' IS kESHAV'
# >>> a.rstrip('iHtISV')
# 'tHIS IS kESHA'

# startswith()
# ------------
# >>> a.startswith('t')
# True
# >>> a.startswith('I')
# False

# endswith()
# ----------
# >>> a.endswith('V')
# True
# >>> a.endswith('I')
# False

# islower()
# ---------
# >>> a='keshav'
# >>> a.islower()
# True
# >>> a='keshav789'
# >>> a.islower()
# True

# isupper()
# ---------
# >>> a.isupper()
# False
# >>> a='KESHAV'
# >>> a.isupper()
# True
# >>> a='KESHAV2374'
# >>> a.isupper()
# True
# >>> a.isupper()
# True

# isalpha()
# ---------
# >>> a.isalpha()
# False
# >>> a='asdlkjLKSJDS'
# >>> a.isalpha()
# True

# isdigit()
# ---------
# >>> a.isdigit()
# False
# >>> a='389KJDkjds'
# >>> a.isdigit()
# False
# >>> a='389'
# >>> a.isdigit()
# True

# isalnum()
# ---------
# >>> a='389KJDkjds'
# >>> a.isalnum()
# True
# >>> a='38'
# >>> a.isalnum()
# True
# >>> a='KJDkjds'
# >>> a.isalnum()
# True
# >>> a='389KJDkjds'
# >>> a.isalnum()
# True
# >>> a=' '

# isspace()
# ---------
# >>> a.isspace()
# True
# >>> a=' hi'
# >>> a.isspace()
# False