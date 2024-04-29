def solution(progresses, speeds):
    
    answer = []
    count = 0
    # index 기준으로 더해주기 -> 100넘어도 계속 진행
    while progresses:
        if progresses[0]>=100:
            progresses.pop(0)
            speeds.pop(0)
            count += 1
            continue
        elif progresses[0]<100 and count:
            answer.append(count)
            count = 0
        else:
            for i in range(len(progresses)):
                progresses[i] += speeds[i]
    
    answer.append(count)
    
    return answer