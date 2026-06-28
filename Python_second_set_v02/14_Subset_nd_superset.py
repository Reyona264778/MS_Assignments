
def user_input():
    l = int(input("Enter the limit : "))
    lst = []
    for i in range(l):
        element = input(f"Enter a element num {i+1}:")
        lst.append(element)
    return lst


def subset_Check(s1,s2):
    s1_check = s1.issubset(s2)
    s2_check = s2.issubset(s1)
    if s1_check==True:
        print(f"{s1} is the subset of {s2}")
    elif s2_check==True:
        print(f"{s2} is the subset of {s1}")
    else:
        print("No subset found")


def disjoin_check(s1,s2):
    s1_check = s1.isdisjoint(s2)
    
    if s1_check==True:
        print(f" disjoint found")
   
    else:
        print("No disjoint found")


def superset_check(s1,s2):
    s1_check = s1.issuperset(s2)
    s2_check = s2.issuperset(s1)
    if s1_check==True:
        print(f"{s1} is the superset of {s2}")
    elif s2_check==True:
        print(f"{s2} is the superset of {s1}")
    else:
        print("No superset found")


list_1 = user_input()
list_2 = user_input()

set_1,set_2 = set(list_1), set(list_2)


print(f"Set 1 : {set_1}")
print(f"Set 2 : {set_2}")

subset_Check(set_1,set_2)
disjoin_check(set_1,set_2)
superset_check(set_1,set_2)

