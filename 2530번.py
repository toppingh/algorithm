# 2530번. 인공지능 시계

A, B, C = map(int, input().split())
D = int(input())

if D >= 60 :
    C += (D % 60)
    if C >= 60 :
        B += 1
        C -= 60
    B += (D / 60)
    if B >= 60 :
        A += (B / 60)
        if A > 23 :
            A = 0
        B %= 60
        

else :
    C += D
    if C >= 60 :
        B += 1
        C -= 60


print("%d %d %d" % (A, B, C))
