dic = {'key1':78,'key2':'val','n':'val'}
val = set(dic.values())
if len(val) == len(dic.values()):
    print("Unique")
else:
    print("Not Unique")
