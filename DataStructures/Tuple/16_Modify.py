tpl1 = (1, "WORLD", 3.5, True,'hello',3.5,'WORLD')
# tpl1[3] = 'New' #shows error
leng = len(tpl1)
val = input("Enter new val : ")
tpl1 = tpl1+(val,)
print(tpl1)