user_list = []
for _ in range(int(input())):
    user_list.append([int(item) if item.isdigit() else item for item in input().split()])
user_list = sorted(user_list, key=lambda x:x[0])
for i in user_list:
    print(i[0],i[1])