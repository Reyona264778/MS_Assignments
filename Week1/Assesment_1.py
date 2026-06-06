#Take all the elements from the tuple and then print it as a list
# tup = (1,5,3,7,2.5)
# lst = []
# for i in tup:
#     lst.append(i)
# print(lst)

#Pattern printing pyramid
row = int(input("Enter the row length :")) 
# loop for assign rows
for i in range(0,row+1):
    # loop for the space before "*"
    for k in range(row-i):
        print(" ", end = " ")
    # loop for the star printing 
    for j in range(1,i*2):
        print ("*",end=" ")
    print()
#in addition for diamond
# for i in range(row-2, 0,-1):
#     for j in range(row-i):
#         print(" ", end = " ")
#     for k in range(1,i*2):
#         print ("*",end=" ")
#     print()
    
    