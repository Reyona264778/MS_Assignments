#Notes
''' Fuction is a blockof code that performs a specific task
    repeat a code == redundant 
    #Recursion : When a function calls itself repeatedly
    '''

heros = ['thor','superman','spiderman','batman']
# def sun(heros):
#     print(len(heros))

# sun(heros)




# def element(heors):
#     # print(heors)
#     for ele in heros:
#         print(ele,end=", ")
# element(heros)



#Fatorial

# n! = 1x2x3x...xn
'''
num = int(input("Enter the value :"))

def fact(num):
    temp = 1
    for i in range(1,num+1):
        temp = temp*i
    print(temp)
fact(num)
'''



# WAF to convert USD to INR

# 1USD == 83INR

# def converter(USD):
#     inr = USD *83
#     print(f"USD = {USD} in INR = {inr}")
# converter(100)





#Recursion
'''def show(n):
    if(n==0):
        return
    print(n)
    show(n-1)
show(5)'''


# write a recursive function to calculate the sum of first n natural numbers
def sum(n):
    if(n==0):
        return 0
    return sum(n-1)+n

s=sum(5)
print(s)


# Write a recursive function to print all elemnts in list Hint: use list& index as parameters