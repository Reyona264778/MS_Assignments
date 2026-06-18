
def UsersEntry():
    limit = int(input("Enter the limit :"))
    lst = []
    for i in range(limit):
        ele = int(input(f"Value {i+1} :"))
        lst.append(ele)
    print(lst)
    return(lst)