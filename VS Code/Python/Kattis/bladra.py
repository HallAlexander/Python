k, q = input().split(' ')
problems = [0] * int(k)
for i in range(int(q)):
    team, problem = input().split(' ')
    problem = int(problem)
    problems[problem - 1] += 1
problems.sort()
print(problems[0])