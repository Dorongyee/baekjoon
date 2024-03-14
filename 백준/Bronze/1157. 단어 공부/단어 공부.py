import collections

word = input()

letters = [i for i in word.upper()]

a = collections.Counter(letters).most_common()

if len(a) > 1 and a[0][1]==a[1][1]:
    print('?')
else:
    print(a[0][0])