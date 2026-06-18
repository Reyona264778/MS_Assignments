tpl = (1, "WORLD", 3.5,(4,2,False,68), True,'hello')

for i in tpl:
    if isinstance(i,tuple):
        print(f"Original Tuple : {tpl}\nValues in nested tuple : {i}")

print(f"Accessing values inside nested tuple : {tpl[3][2]}")
