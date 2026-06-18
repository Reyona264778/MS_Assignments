limit = int(input("Enter the limit :"))
lst = []
for i in range(limit):
    ele = input(f"Value {i+1} :")
    lst.append(ele)


def pharse(val):
    if '.' in val:
        val = float(val)
    elif val.isdigit():
        val = int(val)
    else:
        val = val
    return val


val = input("Enter the element :")
val = pharse(val)
print(f"COUNT :{lst.count(val)}")
