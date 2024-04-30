def solution(answers):
    
    first = [1, 2, 3, 4, 5]
    second = [2, 1, 2, 3, 2, 4, 2, 5]
    third = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    score = [0,0,0]
    
    for i in range(len(answers)):
        if answers[i] == first[i%5]:
            score[0] += 1
        if answers[i] == second[i%8]:
            score[1] += 1
        if answers[i] == third[i%10]:
            score[2] +=1
    if score[0]==score[1] and score[0]==score[2]:
        return [1,2,3]
    elif score[0]==score[1] and score[0] > score[2]:
        return [1,2]
    elif score[0]==score[2] and score[0] > score[1]:
        return [1,3]
    elif score[1]==score[2] and score[1] > score[0]:
        return [2,3]
    else:
        return [score.index(max(score))+1]
    return answer