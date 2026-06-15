#oops Class

# class Microwave:
#     #Initializers
#     def __init__(self) -> None:   #->None it makes extra explicite
#           .
#           .
#           .
# Microwave = Microwave()  #---> Class instantiation type nanetation is not included




# class Dog:

#     def __init__(self,name,breed,owner):
#         self.name = name
#         self.breed = breed
#         self.owner = owner
#     def bark(self):
#         print("Woof woof")

# class Owner:
#     def __init__(self,name,address,cont):
#         self.name = name
#         self.address = address
#         self.cont_no= cont


# owner1 = Owner("Danny","Abc","1234567890")
# d1=Dog("daash","dash",owner1)
# print(d1.owner.name)
# # d1.bark()





# class Person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age

#     def greet(self):
#         print(f"Hello, my name is {self.name} and I am {self.age} years old")

# p1 = Person("Alice",30)
# p1.greet()
# p2 = Person("bob",38)
# p2.greet()


#Accessing and modifying data
#1. The traditional way: make the data private and use getters and setters:



class User:
    def __init__(self,username, email, password):
        self.uname = username
        self.__email = email      #private
        self.pswd = password

    def get_email(self):
        return self.__email.lower().strip()

    # def introo(self, user):
    #     print(f"Hi {user.uname} this is {self.uname} welcome to my page!")

u1 = User("Alice","alice@gmail.com","123")
u2 = User("Bob","bob@gmail.com","abc")


# print(u1.__email)
print(u1.get_email())
u1.__email = "hdgfhdfghgf"
print(u1.get_email())

#The "Consenting Adults" Philosophy

