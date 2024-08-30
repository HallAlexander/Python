def splitString(string, n):
    list = []
    if(n <= len(string)):
        list.extend([string[:n]])
        list.extend(splitString(string[n:], n))
    return list

encryption = input()
key = input()
keyList = splitString(key, 3)
encryption = [*encryption]
for i in range(len(keyList)):
    keyList[i] = int(keyList[i])
    keyList[i] -= 1
for x in keyList:
    print(encryption[x], end='')