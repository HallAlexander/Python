#F(n+1) p will be F(n) q
#F(n+1) q will be F(n)'s (2*(p // q) + 1) * q - p
#// is floor division, so division without remainder

runs = int(input())
for i in range(runs):
    k, set = input().split()
    p, q = map(int, set.split('/'))
    print(k, end=' ')
    print(q, end='/')
    k = (p // q)
    print((2*k + 1) *q - p)