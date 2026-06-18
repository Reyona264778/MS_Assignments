d = {'key1': 1, 'key2': 2, 'key3': None}
value = None
f= 0
for key,val in d.items():
    if val == value:
        print(f"Value found : {key}:{val}")
        f=1
if f ==0:
    print(f"value : {value} NOT FOUND")
