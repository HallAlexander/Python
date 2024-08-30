import math

n, m, k = map(int, input().split())
movie_views = [int(input().split()[1]) for _ in range(n)]
movie_views.sort()

if m == 0:
    passes, optimal_price = 0, 0
elif k == 0:
    passes, optimal_price = n, 0
else:
    pass_value = math.floor(k / m)
    if len(movie_views) - pass_value < 1000000:
        passes = len(movie_views) - pass_value
    else:
        passes = 1000000
    optimal_price = passes * k
    tickets_remaining = 0
    for i in range(passes, len(movie_views)):
        tickets_remaining += movie_views[i] - passes
    optimal_price += (tickets_remaining * m)

print(passes, optimal_price)
