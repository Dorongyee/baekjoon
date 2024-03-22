# "2개의 자연수 a, b(a > b)에 대해서 a를 b로 나눈 나머지가 r일 때, a와 b의 최대공약수는 b와 r의 최대공약수와 같다"
# 이 성질을 이용해서 위의 과정을 계속 반복해 나머지가 0이 나올 때까지 나누면 그 수가 바로 최대공약수.
# 두 수 a와 b의 최소공배수는 a와 b의 곱을 a와 b의 최대공약수를 나눈 것과 같다
def GCD(a,b):
    if a>b:
        if a%b == 0:
            return b
        else:
            return(GCD(b, a%b))
    elif b>a:
        if b%a == 0:
            return a
        else:
            return(GCD(a, b%a))
    else:
        return a

a,b = map(int,input().split())
print(GCD(a, b))
print(int(a*b/GCD(a,b)))