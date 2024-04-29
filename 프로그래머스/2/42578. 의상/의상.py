def solution(clothes):
    dict = {}
    # 같은 의상 종류끼리는 같은 list에 넣어주기
    for i in range(len(clothes)):
        if clothes[i][1] in dict:
            dict[clothes[i][1]] += 1
        else:
            dict[clothes[i][1]] = 1
    
    # 의상 종류 개수별로 더하고, 조합 개수 구해서 더하기
    
    num_list = list(dict.values())    
    num_list = list(map(lambda x:x+1, num_list))
    
    sum = 1
    
    for i in num_list:
        sum *= i
    
    return sum - 1