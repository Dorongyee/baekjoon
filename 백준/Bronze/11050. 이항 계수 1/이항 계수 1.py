def factorial(num):
    i = 1
    for _ in range(2, num + 1):
        i *= _
    return i

n,k = map(int, input().split())

print(int(factorial(n)/factorial(n-k)/factorial(k)))