def people_in_this_room(dp, floor, room_no):
    # 이미 계산된 값이 있는지 확인
    if dp[floor][room_no] != -1:
        return dp[floor][room_no]
    
    # 기본 케이스 처리
    if floor == 0:
        return room_no
    elif room_no == 1:
        return 1
    
    # 재귀적으로 사람 수 계산
    people = 0
    for i in range(1, room_no + 1):
        people += people_in_this_room(dp, floor-1, i)
    dp[floor][room_no] = people  # 계산된 값을 저장
    return people

# 입력 받고 결과 출력
t = int(input())
for _ in range(t):
    floor = int(input())
    room_no = int(input())
    dp = [[-1 for _ in range(room_no + 1)] for _ in range(floor + 1)]  # DP 테이블 초기화
    print(people_in_this_room(dp, floor, room_no))
