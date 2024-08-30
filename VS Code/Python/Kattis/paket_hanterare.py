packages, stores = map(int, input().split())
items_per_store = list(map(int, input().split()))
unique_items = {}
for _ in range(packages):
    item, version = input().split()
    unique_items[item] = int(version)

for i in range(stores):
    version_diff = 0
    for _ in range(items_per_store[i]):
        item, version = input().split(' ')
        version_diff += unique_items[item] - int(version)
    print(version_diff)
