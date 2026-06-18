
lst = ["hello", "", "world"]
lst.remove("")
print(lst)

lst1 = ["hello", "", "world","vfvfdvd"]

new_lst = []

for i in lst1:
    if i != "":
        new_lst.append(i)

print(new_lst)
