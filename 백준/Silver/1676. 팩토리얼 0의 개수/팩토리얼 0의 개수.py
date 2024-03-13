def factorial(num):
    i = 1
    for _ in range(2, num + 1):
        i *= _
    return i

def count_divide(n):
    num = factorial(n)
    count = 0
    while num % 10 == 0:
        num //= 10
        count += 1
    return count

num = int(input())
print(count_divide(num))