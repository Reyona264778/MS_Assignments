d = {'key1': 1, 'key2': 2, 'key3': None}
print(f"Existing dict : {d}")
d['Rename'] = d.pop('key3')

print(f"Updated dict : {d}")