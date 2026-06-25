from os import system
system('cls')
def get_user_input():
    val = input("Enter a string : ")
    val = val.lower()
    return val

def Count_Check(val):
    d = {}
    for i in val:
        if i!=' ':
            d[i] = d.get(i,0) +1
    print(d)

val = get_user_input()
Count_Check(val)
