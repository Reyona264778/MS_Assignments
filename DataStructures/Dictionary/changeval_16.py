d = {'key1': 1, 'key2': 2, 'key3': {'a':1,'b':2}}
print(f"Existing dict : {d}")
d['key3']['b'] = 'new val'

print(f"Updated dict : {d}")