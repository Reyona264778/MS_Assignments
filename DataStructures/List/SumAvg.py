from os import system
from UserInput import UsersEntry
system('cls')

#Sum and average of all numbers in a list

lst=UsersEntry()
sum =0
for i in range(len(lst)):
    sum = sum+lst[i]
avg = sum/len(lst)
print(f"Sum of list elements : {sum}\nAnerage : {avg}")