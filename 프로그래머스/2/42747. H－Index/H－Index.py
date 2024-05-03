def solution(citations):
    citations.sort(reverse=True)
    n = len(citations)
    for i in range(n):
        if citations[i] < i + 1:
            return i
    return n

# 6 5 3 1 0