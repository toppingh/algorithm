word = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

value = input()
cnt = 0

for i in word : 
    value = value.replace(i, '*')
    
print(len(value))
