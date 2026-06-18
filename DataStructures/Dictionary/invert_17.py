def reverse_dict(d):
    rev = {}

    for k, v in d.items():
        
        if isinstance(v, dict):
            rev[k] = reverse_dict(v) 
        else:
            rev[v] = k

    return rev
d = {
    'key1': 1,
    'key2': 2,
    'nested': {'a': 10, 'b': 20}
}

rev = reverse_dict(d)
print(rev)
