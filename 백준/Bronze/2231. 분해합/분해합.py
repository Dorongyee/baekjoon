num = int(input())

for i in range(0, num+1):
    if i == num:
        print(0)
        break
    temp = i
    for j in range(len(str(i))):
        temp += int(str(i)[j])
    if temp == num:
        print(i)
        break