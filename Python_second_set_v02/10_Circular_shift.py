def rotation(lst,d,n):
    if d =='right':
        print(lst[-n:]+lst[:-n])
    if d == 'left':
        print(lst[n:]+lst[:n])
  

lst = [1,2,3,4,5]
d = input("Enter direction : ")
shift = int(input("Enter the shift : "))
rotation(lst,d,shift)