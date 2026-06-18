from UserInput import UsersEntry

lst = UsersEntry()
print("\n Using Inbuilt")
print(f"Maximum : {max(lst)}")
print(f"Minimum : {min(lst)}")

print("\n Manual way:")
mx = lst[0]
mn = lst[0]

for i in range(len(lst)):
    if lst[i]>mx:
        mx = lst[i]
    if lst[i]<mn:
        mn = lst[i]


print(f"Maximum : {mx}")
print(f"Minimum : {mn}")

