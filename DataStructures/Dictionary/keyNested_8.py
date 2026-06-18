d = {'key1':1,'key2':2,'nested':{'history':'value','key2':2},'key3':3}
print(d.get('nested').get('history'))