def solution(participant, completion):
    temp = {}
    
    for i in participant:
        if i in temp:
            temp[i] += 1
        else:
            temp[i] = 1
    
    for i in completion:
        temp[i] -= 1
    
    for key, value in temp.items():
        if temp[key] == 1:
            return key