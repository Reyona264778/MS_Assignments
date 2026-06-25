def merg(*kwargs):
    # d1 = kwargs[0]
    # d2 = kwargs[1]
    res = {}
    for i in kwargs:
        for k,v in i.items():
            if k in res:
                res[k].append(v)
            else:
                res[k] = [v]
    print(res)
d_1 = {'a':1,'b':3}
d_2 = {'b':2, 'c':5}
merg(d_1,d_2)