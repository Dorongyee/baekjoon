while True:
    temp = input()
    if temp == '0':
        break
    else:
        print('yes' if temp == temp[::-1] else 'no')