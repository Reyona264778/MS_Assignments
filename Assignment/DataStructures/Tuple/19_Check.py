tpl1 = (1, "WORLD", 3.5, True,'hello',3.5,'WORLD')
tpl2 = ("Hello","Hello","Hello","Hello")
f=0
for i in tpl2:
    if i!=tpl2[0]:
        f=0
    else:
        f=1
if f ==0:
    print("Not same")
else:
    print("same")
