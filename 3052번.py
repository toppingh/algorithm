A = []

for i in range(10) :
    B = int(input())
    A.append(B % 42)
A = set(A)
print(len(A))
