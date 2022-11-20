Xlist = ['mix', 'xyz', 'apple', 'xanadu', 'rovio']
newlist = []
sort = []

for i in Xlist:
    if i[0][0] == 'x':
        newlist.append(i)

newlist = sorted(newlist)

for i in Xlist:
    if i[0][0] != 'x':
        sort.append(i)

sort = sorted(sort)

for i in sort:
    newlist.append(i)

print(newlist)


