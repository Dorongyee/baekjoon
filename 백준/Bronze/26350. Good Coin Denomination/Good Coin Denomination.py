count = int(input())

for _ in range(count):
    
    temp_list = list(map(int, input().split()))
    print("Denominations:",end=' ')
    TF = True
    for i in temp_list[1:]:
        print(i,end=' ')
    print('')
    for i in range(0, temp_list[0] - 1):
        if temp_list[i + 2] >= (temp_list[i + 1] * 2):
            continue
        else:
            TF = False
            break
    print('Good coin denominations!\n') if TF == True else print('Bad coin denominations!\n')