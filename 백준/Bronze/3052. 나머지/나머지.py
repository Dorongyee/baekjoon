modulo_list = []

for _ in range(10):
    modulo_list.append(int(input())%42)

print(len(list(set(modulo_list))))