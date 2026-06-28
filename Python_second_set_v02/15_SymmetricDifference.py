list_1 = ['101','102','103']
list_2 = ['103','104','105']

result = []

for i in list_1:
    if i not in list_2:
        result.append(i)
for i in list_2:
    if i not in list_1:
        result.append(i)
print(result)