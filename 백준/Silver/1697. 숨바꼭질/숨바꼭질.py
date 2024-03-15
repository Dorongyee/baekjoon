from collections import deque

def bfs(N, K):
    # 최대 위치 값
    MAX = 100001
    # 각 위치에 도달하는 데 걸리는 시간을 저장할 배열
    times = [0] * MAX
    # queue for BFS
    q = deque([N])

    while q:
        current_pos = q.popleft()
        # 현재 위치가 동생의 위치와 같다면 시간을 반환
        if current_pos == K:
            return times[current_pos]
        # 다음으로 이동할 수 있는 위치 확인
        for next_pos in (current_pos - 1, current_pos + 1, current_pos * 2):
            # 다음 위치가 유효하고 아직 방문하지 않았다면
            if 0 <= next_pos < MAX and not times[next_pos]:
                times[next_pos] = times[current_pos] + 1
                q.append(next_pos)

N, K = map(int, input().split())
print(bfs(N, K))
