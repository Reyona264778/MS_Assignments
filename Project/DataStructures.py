# List 

l = [3,5,6,8,"sdft",8.6,"fd",True,34,False]
# l.append(5)
# e = [4,6,3]
# l.extend(e)
# l.insert(1,"New element added through index")
# l.remove(True)   -----> remove the same value from the list

# l.pop(2)          ----> can be pop element from last or can pop element using index

l_sort = sorted(l,key = lambda x:(isinstance(x,str),x))
print(l)

a=10
b= 20
res = lambda a,b: a+b
print(res(a,b))