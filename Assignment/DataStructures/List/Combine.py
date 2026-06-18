l1 = [3,6,"fgh"]
l2 = ['hjl',2.4]

cmb = l1+l2
l1.append(l2)
l1.extend(l2)
print(f"Combined list : {cmb}")
print(f"Combined list using append : {l1}")
print(f"Combined list using extend : {l1}")


