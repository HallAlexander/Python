from decimal import Decimal, getcontext
getcontext().prec = 36
a, b, c = map(int, input().split())
x = Decimal(a) * Decimal(b) / Decimal(c)
print(f"{x:.18f}")
