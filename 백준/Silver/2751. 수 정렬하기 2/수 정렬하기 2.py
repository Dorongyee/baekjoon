num = int(input())
temp_list = []
for _ in range(num):
    temp_list.append(int(input()))

for _ in sorted(temp_list):
    print(_)