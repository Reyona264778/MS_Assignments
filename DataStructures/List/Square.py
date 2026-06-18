#Square of each element in list
from UserInput import UsersEntry

lst=UsersEntry()
sq_lst = []
for i in range(len(lst)):
    sqr = lst[i]*2
    sq_lst.append(sqr)
print(f"Result : {sq_lst}")