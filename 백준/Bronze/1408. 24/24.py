# 시간을 초 단위로 변환하는 함수
def time_to_seconds(h, m, s):
    return h * 3600 + m * 60 + s

# 초 단위를 HH:MM:SS 형식으로 변환하는 함수
def seconds_to_time(seconds):
    h = seconds // 3600
    m = (seconds % 3600) // 60
    s = seconds % 60
    return f"{h:02}:{m:02}:{s:02}"

# 입력 받기
present = list(map(int, input().split(':')))
start = list(map(int, input().split(':')))

# 초 단위로 변환
present_seconds = time_to_seconds(*present)
start_seconds = time_to_seconds(*start)

# 남은 시간 계산 (24시간 처리)
if start_seconds < present_seconds:
    start_seconds += 24 * 3600  # 하루를 더함

remaining_seconds = start_seconds - present_seconds

# 결과 출력
print(seconds_to_time(remaining_seconds))