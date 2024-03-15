def custom_round(number):
    # 소수점 부분
    fractional_part = number - int(number)
    if fractional_part >= 0.5:
        return int(number) + 1
    else:
        return int(number)

n = int(input())
scores = [int(input()) for _ in range(n)]

if scores:
    scores.sort()
    trim_count = custom_round(len(scores) * 0.15)
    trimmed_scores = scores[trim_count:-trim_count] if trim_count > 0 else scores
    avg_score = sum(trimmed_scores) / len(trimmed_scores)
    print(custom_round(avg_score))
else:
    print(0)