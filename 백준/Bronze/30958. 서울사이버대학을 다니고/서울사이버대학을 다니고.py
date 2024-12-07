a = int(input())
string = input()
string = string.replace(' ','')
string = string.replace(',','')
string = string.replace('.','')

alphabet = dict()
for i in string:
    if i in alphabet:
        alphabet[i] += 1
    else:
        alphabet[i] = 1

max_key = max(alphabet, key=alphabet.get)
print(alphabet[max_key])