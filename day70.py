

chars = ['a','b','c','d','e']
i = chars.index('c')
chars = chars[i-3:] + chars[:i+1]
print(chars[3])


# b