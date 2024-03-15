alphabet_list = [chr(a) for a in range(97, 123)]

input_string = input()
for letter in alphabet_list:
    if letter in input_string:
        print(f'{input_string.find(letter)}', end=' ')
    else:
        print(-1, end=' ')