# class Computer:
#     def config(self):
#         print("i5, 16GB, 1TB")
# comp1 = Computer()
# comp1.config()
# Computer.config(comp1)    //This is how the control works

###################################################################################################

#Special method

# class Computer:
#     def __init__(self,deviceID):
#         self.dID = deviceID
#     def config(self):
#         print("1GB, 5GB, 1TB")
#         print(self.dID)
# val = int(input("Enter a value : "))
# comp1 = Computer(val)
# comp1.config()



val = int(input("Entre the limit:"))
rev=0
while val!=0:
    dig = val%10
    rev = rev*10+dig
    val = val//10
print(rev)
