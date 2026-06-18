list1 = [43,'hello','python',90,22]
ele = input("Enter the to be replaced :")
val = input("Enter the new element :")

for i in range(len(list1)):
    if list1[i] == ele :
        list1[i] = val
print(list1)