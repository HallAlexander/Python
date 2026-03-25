teams, matches = map(int, input().split())
rankings = [f'T{i+1}' for i in range(teams)]
for i in range(matches):
    winner, loser = input().split()
    if rankings.index(loser) < rankings.index(winner):
        for j in range(rankings.index(loser),rankings.index(loser)+(rankings.index(winner) - rankings.index(loser))):
            tmp = rankings[j]
            rankings[j] = rankings[j+1]
            rankings[j+1] = tmp
print(*(value for value in rankings))
