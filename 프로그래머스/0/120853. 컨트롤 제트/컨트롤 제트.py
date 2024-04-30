def solution(s):
    
    num_list = s.split()
    sum = 0
    for i in range(len(num_list)):
        if num_list[i] != 'Z':
            sum += int(num_list[i])
        else:
            sum -= int(num_list[i-1])
    
    return sum