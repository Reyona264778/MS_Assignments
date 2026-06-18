import os 
os.system('cls')

# ---------------------------------List-------------------------------------

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

# l = [3,5,6,8,"sdft",8.6,"fd",True,34,False]
# l2 = [0,34,65]
# num = [9,3.9,3.0,1,45,22,1000,5,44,45]
# l.insert(5,l2)
# print(l)
# l.insert(5,5)
# print(l)
# l.remove('sdft')
# l.pop()
# num.sort()
# print(sorted(num, reverse = True))
# val = int(input("Enter the count the number to be searched : "))
# print(num.count(val))
# print(f"Index is found : {num.index(44)}")
# num.clear()
# print(num)

# l.append(5)
# e = [4,6,3]
# l.extend(e)
# l.insert(1,"New element added through index")
# l.remove(True)   -----> remove the same value from the list

# l.pop(2)          ----> can be pop element from last or can pop element using index

# l_sort = sorted(l,key = lambda x:(isinstance(x,str),x))                        #syntax = sorted(iterable, key=function)
# print(l)

#sorted()
# l = [-5,1,3,2,7,-2,-1]
# print(sorted(l,key = lambda x:abs(x)))
# lst = ['apple','banana','zhji','kiwi','alea']
# lst.sort(key = len)
# print(lst)
# print(sorted(lst,reverse =True))




# ---------------------------------TUPLE-------------------------------------
'''
my_tuple.count(2)   # Count occurrences
my_tuple.index(3)   # Find index
del tup
'''
tup = (0,4,2, 1, 2, 3, 4)
# b=()
# a, *b, c = tup
# print(b)
# print(a)
# print(c)
# print(tup.count(2))
# print(tup.index(3))
# del tup
# print(tup)


# ---------------------------------SET-------------------------------------

'''
my_set.add(4)              # Add element
my_set.remove(2)           # Remove element (error if not exist)
my_set.discard(5)          # Safe remove
my_set.pop()               # Remove random element
my_set.clear()             # Empty set

# Set operations
a = {1, 2, 3}
b = {3, 4, 5}

a.union(b)                 # {1,2,3,4,5}
a.intersection(b)          # {3}
a.difference(b)            # {1,2}
a.symmetric_difference(b)  # {1,2,4,5}
'''
# s = set()   # while creating{} it will create empty dictionary it will not create set , so for creating set use typecasting set()
# s = {78,34,"hi","klj",9.08}
# s2 = {56,32,6,34}
# s.add(56)
# s.remove(100)  #showing error
# s.discard(100)   #dosent shows any error
# s.pop(2)         #because of set is unordered the random element is got poped and index wise pop is not possible

# print(s.union(s2))
# print(s)
# print(s2)
# print(s.intersection(s2))
# print(s.difference(s2))        #print values in s and s2  same value
# print(s.symmetric_difference(s2))        #print all values in s and s2 except same value



# ---------------------------------DICTIONARY-------------------------------------
'''
my_dict.get("name")            # Get value
my_dict.keys()                 # All keys
my_dict.values()               # All values
my_dict.items()                # Key-value pairs
my_dict.update({"age": 25})    # Update value
my_dict.pop("age")             # Remove key
my_dict.popitem()              # Remove last item
my_dict.clear()                # Empty dictionary
'''

# dic = {'key1':78,'key2':'val','n':'none'}
# dic.add({"key":65})                     #It will print error
# dic.update({'key3':98})
# print(tuple(dic.keys()))
# print(dic.values())
# print(dic.items())
# dic.pop('n')
# res = dic.pop('y',"NOT FOUND")          #Safe way without getting error if the key is not foud while poping
# print(res)
# dic.popitem()
# print(dic)

# ---------------------------------STRING-------------------------------------

'''
text.upper()        # HELLO WORLD
text.lower()        # hello world
text.title()        # Hello World
text.strip()        # Remove spaces
text.replace("h", "H")
text.split()        # Split into list
text.find("o")      # Find index
text.count("l")     # Count letters
'''
# s = "####**####leArnIng #* pythoN intresting  #########      "
# print(s.upper())
# print(s.lower())
# print(s.title())
# print(s.strip(),'*')
# print(s.lstrip(),'*')
# print(s.rstrip(),'*')
# print(s.rstrip('#'),'*')
# print(s.replace('#','^'))
# text = "hello"
# print(text.split())
# str_List = "apple, banana, grapes"
# print(str_List.split())
# print(s.find("e"))
# print(s.count('e'))
# print('_'.join(text))


