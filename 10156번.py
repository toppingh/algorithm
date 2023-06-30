K, N, M = map(int, input().split())
price = K * N

if price <= M :
    print("0")
else :
    print(price - M)
