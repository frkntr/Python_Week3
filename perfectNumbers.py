

perfectlist = []

for a in range(1, 1001):
    newlist = []
    for i in range(1, a):
        if a % i == 0:
            newlist.append(i)
        else:
            continue
    if sum(newlist) == a:
        perfectlist.append(a)
print("Your Perfect List: ", perfectlist)
