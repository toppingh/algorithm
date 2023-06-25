# Avg = int(A / songs)

# 평균값 = 저작권이 있는 멜로디 개수 / 수록된 곡의 개수

A, I = map(int, input().split())
print(A * (I - 1) + 1)
