# 구매한 각 물건의 가격과 개수를 합한 금액
# 구매한 물건들의 총 금액
# 일치하는지?

# 1번째 줄 -> 영수증 금액 X
# 2번째 줄 -> 물건의 종류 수 N
# N번째 줄 -> 물건의 가격a와 개수b

# 영수증금액 X와 (a*b)가 일치하면 yes 아니면 no

X = int(input())
N = int(input())

total = 0

for i in range(N) :
    a, b = map(int, input().split())
    total += a * b

if (total == X) :
    print("Yes")
else :
    print("No")
