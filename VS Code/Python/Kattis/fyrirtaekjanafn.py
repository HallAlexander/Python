string = input()
res = []
res = ''.join([c for c in string if c in 'aeiouyAEIOUY'])     
print(res)
