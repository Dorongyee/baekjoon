from bisect import bisect_left
import sys
input = sys.stdin.read

def find_LIS(arr, n):
    if n == 0:
        return []

    # 이진 탐색을 위한 배열과 각 요소의 위치 및 부모 추적을 위한 배열
    lis = []
    positions = [-1] * n
    parent = [-1] * n

    for i in range(n):
        # 현재 요소가 들어갈 위치 찾기
        pos = bisect_left(lis, arr[i])
        
        # 부모 위치 설정
        if pos > 0:
            parent[i] = positions[pos-1]
        
        # lis 배열 갱신
        if pos < len(lis):
            lis[pos] = arr[i]
        else:
            lis.append(arr[i])
        
        # 위치 저장
        positions[pos] = i

    # LIS 복원
    lis_length = len(lis)
    lis_result = [0] * lis_length
    k = positions[lis_length-1]
    for i in range(lis_length-1, -1, -1):
        lis_result[i] = arr[k]
        k = parent[k]

    return lis_length, lis_result

# 입력 처리
data = input().split()
n = int(data[0])
arr = list(map(int, data[1:n+1]))

# LIS 계산
lis_length, lis_result = find_LIS(arr, n)

# 결과 출력
print(lis_length)
print(" ".join(map(str, lis_result)))
