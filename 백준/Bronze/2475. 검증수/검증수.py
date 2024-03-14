list = map(int,input().split())
print(sum([item**2 for item in list])%10)