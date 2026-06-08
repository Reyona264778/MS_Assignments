#LIST

bag = ["var","int",456,7.8,4+4j]

print("Bag variable contain : ",bag)

# print(bag[2:])
# print(bag[::-1])
# print(bag[:])
# val = "Program"
# after_Iter = []
# for i in val:
#     after_Iter.append(i)
# print(after_Iter)

# bag.insert(2,"Cherry")
# print("After inserting : ", bag)

# even_num = [2,6,8.4]
# odd_num = [1,3,5,7,9]
# bag.extend(even_num) // append the each element to the list
# bag.append(odd_num) // append the whole index
# print("List after extending : ", bag)

# bag.reverse()
# print(bag)

    #reversed() ---> function

# food = ['biriyani', 'pastha', 'mandi', 'noodles']
# for i in reversed(food):
    # print(list(i))

num = [2,5.11,67,32,56,12]
# num.sort()
# print("After sorting : ", num)
# rev_sort = num.sort(reverse = True) //this gives None as output because of list.sort() sorts the list in-place It does NOT return any thing, So Python automatically assigns None to rev_sort
num.sort(reverse =True)
print("Ater reverse sorting :",num)