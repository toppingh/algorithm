A = int(input())

for i in range(A) :
    score = 0
    num = 0
    value = input()
    for ox in value :
        if ox == "X" :
            num = 0
        elif ox == "0" :
            num += 1
            score += num
    
    print(score)
