C = int(input())

for i in range(C) :
    N = list(map(int, input().split()))
    avg = sum(N[1:]) / N[0]
    over = 0

    for k in N[1:] :
        if k > avg :
            over += 1
    su = over / N[0] * 100
    print("{:.3f}%".format(su))
