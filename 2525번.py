A, B = map(int, input().split(" "))
C = int(input())

if B + C < 60 :
    B += C

elif B + C == 60 :
    if A < 23 :
        A += 1
    elif A >=23 :
        A = 0
    B = 0

elif B + C > 60 :
    over = ((B + C) // 60)
    if A + over <= 23 :
        A += over

    elif A + over >= 23 :
        A += over - 24

    B += C - (over * 60)

    if A == 60 :
        A = 0

print(int(A), B)
