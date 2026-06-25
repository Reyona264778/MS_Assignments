def get_user_input():
    val1 = input("Enter 1st string : ")
    val2 = input("Enter 2nd string : ")
    return val1.lower(),val2.lower()

def Checker(*val):
    d = {}
    d2 = {}
    if len(val)==2:
        s1,s2 =val[0],val[1]
        for s in s1:
            d[s] = d.get(s,0) + 1
        for s in s2:
            d2[s] = d2.get(s,0) + 1
        if d.items()==d2.items():
            print("Anagram")
        else:
            print("Not Anagram")

val_1,val_2 = get_user_input()
Checker(val_1,val_2)