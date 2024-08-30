cases = int(input())
for _ in range(cases):
    input()
    godzilla_size, mecha_size = map(int, input().split())
    godzilla = map(int, input().split())
    mecha = map(int, input().split())
    mecha = list(sorted(mecha))
    godzilla = list(sorted(godzilla))

    while(godzilla_size != 0 and mecha_size != 0):
        if(godzilla[0] > mecha[0]):
            mecha.pop(0)
            mecha_size -= 1
        elif(mecha[0] > godzilla[0]):
            godzilla.pop(0)
            godzilla_size -= 1
        elif(mecha[0] == godzilla[0]):
            mecha.pop(0)
            mecha_size -= 1
    if(len(godzilla) == 0):
        print('mechaGodzilla')
    elif(len(mecha) == 0):
        print('Godzilla')
