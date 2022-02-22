def self(num) :
    num += sum(map(int, str(num)))
    return num

a = [0] * 10001
for i in range(1, 10001) :
    a[i] = self(i)

for i in range(1, 10001) :
    if (i not in a) :
        print(i)
