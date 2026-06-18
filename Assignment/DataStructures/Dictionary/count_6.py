d = {'username':'reyona','company': 'ust'}

ch = input("Enter the string : ")
# s = ch.split()
fq = {}
for i in range(len(ch)):
    fq.update({i:ch[i]})
print(fq)