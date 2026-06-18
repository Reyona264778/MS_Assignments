from os import system

system('cls')
def viewList(lst):
    print(f"\nList : {lst}")

def pharse(val):
    if '.' in val:
        val = float(val)
    elif val.isdigit():
        val = int(val)
    else:
        val = val
    return val

def appendFun(lst):
    num = input("Enter the value : ")
    num = pharse(num)
    lst.append(num)
    viewList(lst)

def extendFun(lst):
    print("\n**Note : Hey you can enter nultiple values..Lets try!!**")
    num = input("Enter the values : ")
    values = num.split(',')
    new =[]
    for v in values:                 
        v = v.strip()           
        new.append(pharse(v)) 
    lst.extend(new)
    viewList(lst)

def insertFun(lst):
    val = input("Enter the element :")
    ind = int(input("Prefered index : "))
    v = pharse(val)
    lst.insert(ind,v)
    viewList(lst)

def countFun(lst):
    viewList(lst)
    val = input("Enter the element :")
    val = pharse(val)
    print(f"COUNT :{lst.count(val)}")

def indexFun(lst):
    val = input("Enter valid element : ")
    ind=[]
    val = pharse(val)
    for i in range(len(lst)):
        if lst[i] == val:
            ind.append(i)
    print(f"\n{val} is found in index : {ind}")

def sortFun(lst):
    print(f"\nBefore sort :")
    viewList(lst)
    lst.sort()
    print(f"After Sort : {lst}")

def revFun(lst):
    viewList(lst)
    lst.reverse()
    print(f"\nReversed : {lst}")

def rmvFun(lst):
    viewList(lst)
    num = input("Enter the element to be removed : ")
    num = pharse(num)
    lst.remove(num)
    viewList(lst)

def popFun(lst):
    c = input("Do you want to pop element from index(y/n)")
    if c=='y':
        ind = int(input("Enter the valid index :"))
        lst.pop(ind)
        viewList(lst)
    else:
        print("\nSussessfully poped out")
        lst.pop(ind)
        viewList(lst)

'''
my_list.append(4)        # Add element at end
my_list.insert(1, 10)    # Insert at index

my_list.remove(2)        # Remove value
my_list.pop()            # Remove last item
my_list.pop(1)           # Remove by index

my_list.sort()           # Sort list
my_list.reverse()        # Reverse list
my_list.count(3)         # Count occurrences
my_list.index(10)        # Find index
my_list.clear()          # Empty list

'''
def choiceFun(lst):
    while True:
        print("\nChoose your choice:")
        print("1. Append")
        print("2. Extend")
        print("3. Insert")
        print("4. Count")
        print("5. Index")
        print("6. Sort")
        print("7. Reverse")
        print("8. Remove")
        print("9. Pop")
        print("10. View")
        print("11. Clear")
        print("0 to exit")

        choice = int(input("Enter your choice: "))

        match choice:
            case 1:
                system('cls')
                print("\nAppend selected")
                appendFun(lst)

            case 2:
                system('cls')
                print("\nExtend selected")
                extendFun(lst)

            case 3:
                system('cls')
                print("\nInsert selected")
                insertFun(lst)

            case 4:
                system('cls')
                print("\nCount selected")
                countFun(lst)

            case 5:
                system('cls')
                print("\nIndex selected")
                indexFun(lst)

            case 6:
                system('cls')
                print("\nSort selected")
                sortFun(lst)
            
            case 7:
                system('cls')
                print("\nReverse selected")
                revFun(lst)

            case 8:
                system('cls')
                print("\nRemove selected")
                rmvFun(lst)

            case 9:
                system('cls')
                print("\nPop selected")
                popFun(lst)

            case 10:
                system('cls')
                print("\nView selected")
                viewList(lst)

            case 11:
                print("\nClearing....")
                lst.clear()
                viewList()
            case 0:
                return 0 



def basic_list_operations():
    n = int(input("Enter the range of elements : "))
    lst = []

    for i in range(n):
        val = input(f"Value {i+1} : ")
        lst.append(pharse(val))
    
    system('cls')
    viewList(lst)
    choiceFun(lst)


    # print(type(lst[1]))
basic_list_operations()