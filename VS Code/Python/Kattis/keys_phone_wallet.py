items = int(input())
lst = []
forgot = False
for i in range(items):
    lst.append(input())
if 'keys' not in lst:
    print('keys')
    forgot = True
if 'phone' not in lst:
    print('phone')
    forgot = True
if 'wallet' not in lst:
    print('wallet')
    forgot = True
if forgot == False:
    print('ready')
