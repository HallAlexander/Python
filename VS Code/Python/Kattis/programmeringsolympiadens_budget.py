n = int(input())
budget = 0
for _ in range(n):
    input()
    budget += int(input())
if budget > 0:
    print('Usch, vinst')
elif budget < 0:
    print('Nekad')
else:
    print('Lagom')