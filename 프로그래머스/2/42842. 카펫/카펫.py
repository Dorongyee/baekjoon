def solution(brown, yellow):
    # [x,y]
    # brown = 2x+2y-4
    # yellow = xy-2x-2y+4    
    possible_list = []
    area = brown + yellow
    
    length = 3
    while length < area / 2:
        if area % length == 0 and (area/length) > 2:
            possible_list.append([length,area//length])
        length += 1
        
    possible_list.sort(reverse=True)
    
    for i in possible_list:
        if (i[0]+i[1]-2) * 2 == brown:
            return i