val1 = input("Enter 1st string : ")
words = val1.split()
print(words)


for w in words:
    print(w[::-1],end=" ")

