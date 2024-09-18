numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
prims = []
not_prims = []
for i in numbers:
    flag = True
    if i == 1:
        continue
    for j in range(2, i):
        if i % j == 0:
            flag = False
            break
    if flag == True:
        prims.append(i)
    else:
        not_prims.append(i)
print(prims)
print(not_prims)
