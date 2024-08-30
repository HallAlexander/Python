beer = int(input())
lemonade = int(input())
if beer == 0 or lemonade == 0:
    print(0)
elif beer <= lemonade:
    print(beer*2)
elif lemonade <= beer:
    print(lemonade*2)
