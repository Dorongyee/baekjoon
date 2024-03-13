def sort_by_order_length(temp_list):
    duplicate_deleted = list(set(temp_list))
    sorted_list = sorted(duplicate_deleted)
    sorted_list_by_length = sorted(sorted_list,key=len)
    for i in sorted_list_by_length:
        print(i)
    return 0
def process_input():
    num = int(input())
    word_list = [input() for i in range(num)]
    return sort_by_order_length(word_list)
process_input()