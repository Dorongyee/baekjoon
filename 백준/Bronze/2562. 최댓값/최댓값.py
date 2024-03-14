num_list = []
for _ in range(9):
    num_list.append(int(input()))
sorted_num_list = sorted(num_list)
print(sorted_num_list[-1])
print(num_list.index(sorted_num_list[-1])+1)