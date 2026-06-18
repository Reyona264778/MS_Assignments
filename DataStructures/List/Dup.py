def pharse(val):
    if '.' in val:
        val = float(val)
    elif val.isdigit():
        val = int(val)
    else:
        val = val
    return val

limit = int(input("Enter the limit :"))
lst = []
for i in range(limit):
    ele = input(f"Value {i+1} :")
    ele = pharse(ele)
    lst.append(ele)

print(list(set(lst)))
