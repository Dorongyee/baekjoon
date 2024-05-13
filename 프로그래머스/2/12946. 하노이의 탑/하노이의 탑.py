def solution(n):
    # 원판을 한 기둥에서 다른 기둥으로 옮기는 과정을 담을 리스트
    answer = []
    
    # 재귀적으로 하노이의 탑 문제를 해결하는 함수
    def move(n, start, to, via):
        # n개의 원판을 start에서 to로 옮기는데 via를 보조 기둥으로 사용
        if n == 1:
            # 1개의 원판을 직접 이동
            answer.append([start, to])
        else:
            # n-1개를 via를 목적지로 하여 이동
            move(n - 1, start, via, to)
            # 가장 큰 원판을 목적지로 이동
            answer.append([start, to])
            # n-1개를 via에서 to로 최종 목적지로 이동
            move(n - 1, via, to, start)
    
    # 처음 호출: 1번 기둥에서 3번 기둥으로, 2번을 보조 기둥으로 사용
    move(n, 1, 3, 2)
    
    return answer
