emp = [{'name':'A','salary':50000},
       {'name':'B','salary':59000},
       {'name':'C','salary':69000}]

emp.sort(key = lambda emp: emp['salary'],reverse=True)
print(emp)