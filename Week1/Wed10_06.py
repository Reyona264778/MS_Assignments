#OOPS Concept

# def sum_(a,b):
#     return a+b

# def diff(a,b):
#     return a-b
# def mul(a,b):
#     return a*b

# def div(a,b):
#     return a/b

# def fun(arg1,arg2):    #Higher order functions
#     print(arg1(3,7) , arg2(8,9))

# fun(sum_ , div)


# def process(func, text):
#     return func(text)

# def uppercase(text):
#     return text.upper()

# print(process(uppercase, "hello"))

#===========================================================================================
#Global and local variable

# global_var = 1000

# def fun():
#     global_var = 200
#     return global_var
#     # print(f"Global_var inside fun value is {Global_var}")
# print(f"Global_var outside fun value is {global_var}")
# print(fun())



for row in range(1,11):
    for col in range(row,):
        print("*",end = " ")