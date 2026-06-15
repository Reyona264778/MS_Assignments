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

###################################################################################################


# val = int(input("Entre the limit:"))
# rev=0
# while val!=0:
#     dig = val%10
#     rev = rev*10+dig
#     val = val//10
# print(rev)

###################################################################################################


#MATCH

val1 = int(input("enter a number : "))
val2 = int(input("Enter a number : "))

print("\n1. sum\n2. Difference\n3. Division\n4. Multiplication")

c = int(input("Enter your choice:"))
match c:
    case 1:
        print(val1+val2)
    case 2:
        print(val1-val2)
    case 3:
        print(val1/val2)
    case 4:
        print(val1*val2)
    case _:
        print("No match found")
