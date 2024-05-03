standard1 = ['WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW']
standard2 = ['BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB']

def string_diff(str1, str2):
    diff_count = 0
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            diff_count += 1
    return diff_count

def difference(standard, board):
    difference_sum = 0
    for i in range(8):
        difference_sum += string_diff(standard[i], board[i])
    return difference_sum

def choose(board, n, m):
    returningboard = []
    for i in range(n, n + 8):
        returningboard.append(board[i][m:m + 8])
    return returningboard
##########################################
a, b = map(int, input().split())
chessboard = [input() for _ in range(a)]

fix_num_list = []

for i in range(a - 7):
    for j in range(b - 7):
        board = choose(chessboard, i, j)
        fix_num_list.append(min(difference(standard1, board), difference(standard2, board)))

print(min(fix_num_list))
