def solution(clothes):
    from collections import defaultdict
    clothes_dict = defaultdict(int)
    
    # 각 의상 종류에 따라 의상의 개수를 셈
    for _, category in clothes:
        clothes_dict[category] += 1

    answer = 1
    # 각 종류별로 의상 선택 옵션 계산 (의상 개수 + 1)
    for count in clothes_dict.values():
        answer *= (count + 1)
    
    # 모든 의상을 선택하지 않는 경우의 수 1을 빼서 반환
    return answer - 1
