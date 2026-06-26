d = {"Orwell":["1984","Animal Farm"],
     "Huxley":["Brave New world"]}
res = {}
for k,v in d.items():
    for b in v:
        res[b] = k
print(res)
    
