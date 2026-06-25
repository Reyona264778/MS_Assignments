def rotation(lst,d,n):
    if d =='right':
        print(lst[-2:]+lst[:-2])
    
  

lst = [1,2,3,4,5]
d = input("Enter direction : ")
shift = int(input("Enter the shift : "))
rotation(lst,d,shift)