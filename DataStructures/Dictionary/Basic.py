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