count = int(input())
coordinate_list = []
for i in range(count):
    coordinate_list.append(list(map(int, input().split())))
coordinate_list = sorted(coordinate_list)
for coordinate in coordinate_list:
    print(coordinate[0],coordinate[1])