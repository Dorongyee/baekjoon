alphabet_letter = [chr(i) for i in range(97,123)]

temp = int(input())
hash = 0
string = input()
for i in range(temp):
    hash += ((alphabet_letter.index(string[i]) + 1) * (31**i))

print(hash % 1234567891)