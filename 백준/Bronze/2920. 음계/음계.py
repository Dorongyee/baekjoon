num_list = input().split()
num_list = [int(item) for item in num_list]
if num_list == sorted(num_list):
    print('ascending')
elif num_list == sorted(num_list, reverse=True):
    print('descending')
else:
    print('mixed')