n, k = map(int,input().split())

numbers = list(range(1, n + 1))
pop_index = 0
picked_list = []

for i in range(n):
    pop_index = (pop_index + k - 1) % len(numbers)
    picked_list.append(numbers.pop(pop_index))

print("<" + ", ".join(map(str, picked_list)) + ">")
