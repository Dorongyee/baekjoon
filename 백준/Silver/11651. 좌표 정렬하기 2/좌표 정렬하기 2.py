count = int(input())
coordinate_list = []
for i in range(count):
    coordinate_list.append(list(map(int, input().split())))
coordinate_list = sorted(coordinate_list,key = lambda x:(x[1],x[0]))
for coordinate in coordinate_list:
    print(coordinate[0],coordinate[1])