from os import system
def cls():
    system('cls')

def pharseFun(val):
    if '.' in val:
        val=float(val)
    elif val.isdigit():
        val = int(val)
    else:
        val=val
    return val

def clearFun(d):
    d.clear()
    return d

def viewFun(d):
    print("\nDICTIONARY")
    
    print("{ ")

    for k, v in d.items():
        print(f"\t{k} : {v}")

    print("}")

    return d

def copyFun(d):
    x = d.copy()
    return x


def choicesFun(dict):
    while True:
        print("\nChoose your choice:")
        print("1. Clear")
        print("2. View")
        print("3. Copy")
        print("4. Fromkeys")
        print("5. Get")
        print("6. Items")
        print("7. Keys")
        print("8. Pop")
        print("9. Popitem")
        print("10. setdefault")
        print("11. Update")
        print("12. Values")
        print("0 to exit")
        c = int(input("Your choice : "))
        match c:
            case 1:
                clearFun(dict)
                viewFun(dict)
            case 2:
                print("View Dictionary")
                viewFun(dict)
            case 3:
                print("\nCopy Function")
                res = copyFun(dict)
                print(f"The Copied dict = {res}")

            case 0:
                return 0



def dict_Basic():
    dict = {}
    l = int(input("Enter the Limit : "))
    for i in range(l):
        print(f"\nKEY VALUE PAIR - {i+1} ")
        key = input("KEY : "); key = pharseFun(key)
        val = input("VALUE :"); val = pharseFun(val)
        dict.update({key:val})

    choicesFun(dict)
    return dict
cls()
dict_Basic()









dic = {'key1':78,'key2':'val','n':'none'}
print(dic.get("key2"))
# dic.add({"key":65})#It will print error
dic.update({'key3':98})
print(tuple(dic.keys()))
print(dic.values())
print(dic.items())
dic.pop('n')
res = dic.pop('y',"NOT FOUND")          #Safe way without getting error if the key is not foud while poping
print(res)
dic.popitem()
print(dic)