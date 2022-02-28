A = input()
num = 0

for i in A :
    if ord(i) <= 67 :
        num += 3
    elif ord(i) <= 70 :
        num += 4
    elif ord(i) <= 73 :
        num += 5
    elif ord(i) <= 76 :
        num += 6
    elif ord(i) <= 79 :
        num += 7
    elif ord(i) <= 83 :
        num += 8
    elif ord(i) <= 86 :
        num += 9
    else :
        num += 10

print(num)
