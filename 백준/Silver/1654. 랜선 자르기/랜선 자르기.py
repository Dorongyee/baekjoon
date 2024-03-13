def calculate_num(num, line_list):
    start, end = 1, max(line_list)
    result = 0
    while start <= end:
        mid = (start + end) // 2
        total = sum(line // mid for line in line_list)
        if total >= num:
            result = mid
            start = mid + 1
        else:
            end = mid - 1
    return result

def process_input():
    k, n = map(int, input().split())
    lines = [int(input()) for _ in range(k)]
    return calculate_num(n, lines)

print(process_input())