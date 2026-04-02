weight, stacks = map(int, input().split())
coins = (stacks*(stacks+1))/2
gold_stack = int((weight - (coins * 29260)) / 110)
print(gold_stack)