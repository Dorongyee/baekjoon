def solution(citations):
    citations.sort(reverse=True)
    n = len(citations)
    # 인용횟수가 전부 전체 갯수 이상인경우 h index는 논문 수; return n
    # 그렇지 않은 경우부터
    for i in range(n):
        if citations[i] < i + 1:
            return i
    return n

# 6 5 3 1 0