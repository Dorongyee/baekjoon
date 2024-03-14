temp = int(input())
temp *= int(input())
temp *= int(input())
num_string = str(temp)

nums = [0,1,2,3,4,5,6,7,8,9]
nums = list(map(str,nums))
for num in nums:
    print(num_string.count(num))