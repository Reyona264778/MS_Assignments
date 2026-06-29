lst = [1,2,3,4,5,1,6,6]
s = set()
unique = []
for i in lst:
    if i not in unique:
        unique.append(i)
    else:
        s.add(i)
print(s)