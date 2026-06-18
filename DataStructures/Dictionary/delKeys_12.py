d = {'key1': 1, 'key2': 1, 'key3': 1}

k = ['key1','key3']

for key in k:
    if key in d :
        d.pop(key)
print(d)