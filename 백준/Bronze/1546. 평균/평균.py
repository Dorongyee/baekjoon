temp = int(input())

score_list = list(map(int, input().split()))
score_list = list(map(lambda x: x/max(score_list)*100, score_list))
print(sum(score_list)/temp)