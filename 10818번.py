N = int(input())
su = N
new_N = 0
cycle_N = 0

while True :
    a = su
    b = su % 10
    c = (a + b) % 10
    su = (b * 10) + c

    cycle_N += 1
    if(su == N):
        break

print(cycle_N)
