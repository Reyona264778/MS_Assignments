tpl1 = (1, "WORLD", 3.5, True,'hello')
tpl2 = (4,7,'s')
print(f"Before swap : \ntuple 1 = {tpl1}\ntuple 2 = {tpl2}")
tpl3 = tpl2
tpl2 = tpl1
tpl1 = tpl3
print(f"After swap : \ntuple 1 = {tpl1}\ntuple 2 = {tpl2}")
