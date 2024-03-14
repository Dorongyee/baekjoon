stack_size = int(input())
append_num = 1
answer_sequence = []
compare_list = []
compare_index = 0
push_pop_list = []

for i in range(stack_size):
    # 숫자 먼저 받고
    temp_num = int(input())
    answer_sequence.append(temp_num)

while append_num <= stack_size:
    # 현재 리스트와 비교 먼저
    if compare_list and (answer_sequence[compare_index] == compare_list[-1]):
        push_pop_list.append('-')
        compare_list.pop()
        compare_index += 1
        continue
    # 1부터 하나씩 stack에 밀어넣고
    else:
        compare_list.append(append_num)
        push_pop_list.append('+')
        append_num += 1

while compare_list:
    if answer_sequence[compare_index] == compare_list[-1]:
        push_pop_list.append('-')
        compare_list.pop()
        compare_index += 1
    else:
        push_pop_list.append("NO")
        break

if 'NO' in push_pop_list:
    print("NO")
else:
    while push_pop_list:
        print(push_pop_list.pop(0))