Yl = ["xxx", "aaa", "r5t6yy", "g", 'wow']
counter = 0

for i in Yl:
    if i[0][0] == i[-1] and len(i) >= 2:
        counter = counter +1

print(counter)