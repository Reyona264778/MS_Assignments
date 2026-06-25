dict_a = {'a':10,'b':20}
dict_b = {'b':5, 'c':15}

def Merge_Dicts(*kwargs):
    merged_dict = {}
    for d in kwargs:
        for k,v in d.items():
            merged_dict[k] = merged_dict.get(k,0)+v
    print(merged_dict)

Merge_Dicts(dict_a,dict_b)
    