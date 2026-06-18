list1 = [3,5,2,{'key1':'val1','key2':'val2'},'str']

for i in range(len(list1)):
    if isinstance(list1[i],dict):
        print(list1[i])
