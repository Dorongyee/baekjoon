def solution(array, commands):
    answer = []
    
    for i in range(len(commands)):
        if commands[i][0] == commands[i][1]:
            answer_num = array[commands[i][0]-1]
            answer.append(answer_num)
        else:
            modified_array = array[commands[i][0]-1:commands[i][1]]
            modified_array.sort()
            answer.append(modified_array[commands[i][2]-1])
    
    return answer