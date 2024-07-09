import math

def count_square_free_numbers(min_val, max_val):
    length = max_val - min_val + 1
    is_square_free = [True] * length
    limit = int(math.sqrt(max_val)) + 1

    for i in range(2, limit):
        square = i * i
        # min_val 이상에서 square의 배수가 되는 가장 작은 수를 찾는다.
        start = ((min_val + square - 1) // square) * square
        
        # start부터 max_val까지 square의 배수를 모두 False 처리
        for j in range(start, max_val + 1, square):
            is_square_free[j - min_val] = False

    # True, 즉 제곱ㄴㄴ수의 개수를 세서 반환
    return sum(is_square_free)

# 입력 받기
min_val, max_val = map(int, input().split())
# 제곱ㄴㄴ수 개수 출력
print(count_square_free_numbers(min_val, max_val))
