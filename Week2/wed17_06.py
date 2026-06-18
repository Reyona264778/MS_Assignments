from os import system

system('cls')
'''
#Arbitarary arguments

def fun(*args):
    a,b,d,e = args
    d = a+b
    c= d*e
    print(f"{a}+{b} = {d}")
    print(f"{d}*{e} = {c}")

fun(4,2,5,1)

def Dic(**kwargs):
    for key,val in kwargs.items():
        print(f"{key} : {val}")


Dic(name="Reyona",age=22,company='UST')

'''
#-------------------------------------------------------------------------------------------------
