a = int(input())
answer = 1
if (a == 0) or (a == 1):
    print(1)
else:
    for i in range(1,a+1):
        answer *= i
    print(answer)