lst = [1,2,3,4]

op = [()]
for i in lst:
    op.append((i,))
for j in range(len(lst)):
    for k in range(j+1,len(lst)):
        op.append((lst[j],lst[k]))

print(op)

