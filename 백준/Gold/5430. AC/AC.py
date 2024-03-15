from collections import deque

test = int(input())

for _ in range(test):
    # 수행할 함수 입력
    p = input()
    # 배열의 크기 입력
    n = int(input())
    # 배열 입력
    arr_input = input().strip('[]')
    array = deque(map(int, arr_input.split(','))) if arr_input else deque()
    
    # R과 D 함수의 실행 상태 관리 변수
    is_reversed = False
    is_error = False
    
    for function in p:
        if function == 'R':
            is_reversed = not is_reversed
        elif function == 'D':
            if array:
                # 배열이 비어있지 않을 경우, 첫 번째 원소 제거.
                if is_reversed:
                    array.pop()  # 뒤집힌 상태에서는 마지막 원소 제거.
                else:
                    array.popleft()  # 원래 상태에서는 첫 번째 원소 제거.
            else:
                # 배열이 비어있을 경우, 에러 표시하고 루프 종료.
                is_error = True
                break
    
    if is_error:
        print('error')
    else:
        if is_reversed:
            array.reverse()  # 배열이 뒤집힌 상태라면, 최종적으로 뒤집어서 출력.
        print('[' + ','.join(map(str, array)) + ']')