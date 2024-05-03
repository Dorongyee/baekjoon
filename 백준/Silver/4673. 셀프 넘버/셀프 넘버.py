not_self = []
for i in range(10000):
    SUM = i
    for n in range(len(str(i))):
        SUM += int(str(i)[n])
    not_self.append(SUM)

self = {i for i in range(10001)}
self = sorted(list(self - set(not_self)))
for i in self:
    print(i)