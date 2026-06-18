tpl1 = (1, "WORLD", 3.5, True,'hello',3.5,'WORLD')
print(tuple(filter(lambda x : isinstance(x,(int,float)) and x%2!=0 , tpl1)))