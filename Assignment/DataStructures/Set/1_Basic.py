s = set()   # while creating{} it will create empty dictionary it will not create set , so for creating set use typecasting set()
s = {78,34,"hi","klj",9.08}
s2 = {56,32,6,34}
s.add(56)
s.remove(100)  #showing error
s.discard(100)   #dosent shows any error
s.pop(2)         #because of set is unordered the random element is got poped and index wise pop is not possible

print(s.union(s2))
print(s)
print(s2)
print(s.intersection(s2))
print(s.difference(s2))        #print values in s and s2  same value
print(s.symmetric_difference(s2))  