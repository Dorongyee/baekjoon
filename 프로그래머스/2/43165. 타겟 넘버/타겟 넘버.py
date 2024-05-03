def solution(numbers, target):
    count = 0
    total_combinations = 2 ** len(numbers)  # 가능한 조합의 수

    for i in range(total_combinations):
        current_sum = 0

        for j in range(len(numbers)):
            # i의 j번째 비트를 확인하여 + 또는 - 연산을 결정
            if i & (1 << j):
                current_sum += numbers[j]
            else:
                current_sum -= numbers[j]
        
        if current_sum == target:
            count += 1

    return count

