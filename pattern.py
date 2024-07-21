
a = ['A','B','C','D','E','F']

for l in range(len(a)):
    for i in range(l+1):
        a[-1-i] = a[-1-l]
    print(a)