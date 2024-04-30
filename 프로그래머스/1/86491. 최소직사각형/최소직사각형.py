def solution(sizes):
    # 전체 정렬 해주고(가로세로 돌릴수 있으니 상관없음)
    for i in range(len(sizes)):
        sizes[i].sort(reverse=True)
    sizes.sort(reverse=True)
    # 최대값 * 최대값
    max_x = sizes[0][0]
    max_y = 0
    for i in range(len(sizes)):
        if sizes[i][1]>max_y:
            max_y = sizes[i][1]
    return max_x * max_y