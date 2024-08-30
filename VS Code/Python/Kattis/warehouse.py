def bubble2Sort(arr, arr2):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] < arr[j+1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                arr2[j], arr2[j + 1] = arr2[j + 1], arr2[j]
                swapped = True
            elif arr[j] == arr[j+1]:
                if arr2[j + 1] < arr2[j]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    arr2[j], arr2[j + 1] = arr2[j + 1], arr2[j]            
                    swapped = True
        if (swapped == False):
            break


runs = int(input())
for i in range(runs):
    shipments = int(input())
    tmp_item = ''
    tmp_no = 0
    item_lst = []
    no_lst = []
    for j in range(shipments):
        tmp_item, tmp_no = input().split(' ')
        tmp_no = int(tmp_no)
        if tmp_item in item_lst:
            no_lst[item_lst.index(tmp_item)] += tmp_no
        else:
            item_lst.append(tmp_item)
            no_lst.append(tmp_no)
    bubble2Sort(no_lst, item_lst)
    print(len(item_lst))
    for j in range(len(item_lst)):
        print(item_lst[j], end=' ')
        print(no_lst[j])
