import decimal
n = int(input())
decimal.getcontext().prec = n + 10

print(f"{decimal.Decimal(10)**-n:.{n}f}")