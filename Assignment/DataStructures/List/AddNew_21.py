list1 = [3,8,3,5,"python",6]

print(f"List : {list1}")
val = input("Enter the new element :")
spec = input("Enter the specified element :")
found = False
for i in range(len(list1)):
    if list1[i] == spec:
        list1.insert(i+1,val)
        found = True
        break
if not found:
    print("Not Found")
print(list1)


