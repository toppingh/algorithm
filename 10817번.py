numList = list(map(int, input().split()))

numList.remove(max(numList))
numList.remove(min(numList))

print(numList[0])
