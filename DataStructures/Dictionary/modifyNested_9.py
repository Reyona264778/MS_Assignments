d = {'key1':1,'key2':2,'nested':{'history':'value','key2':2},'key3':3}
d['nested']['history'] = 'Freedom'
print(f"history:",d.get('nested').get('history'))
print(f"history:",d['nested']['history'])
