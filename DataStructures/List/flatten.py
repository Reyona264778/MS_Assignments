
def flatten(lst):
    flat = []

    for i in lst:
        if isinstance(i, list):
            flat.extend(flatten(i))   # recursive call
        else:
            flat.append(i)

    return flat

lst = [1,[43,54,[56,9],80],52,12]
res = flatten(lst)
print(res)