lst = [1,2,2,3,1,4,2]
c = []
for i in lst:
    if i not in c:
        c.append(i)
print(c)