a = []
s = []
for i in range(6):
    a.append(list(map(int, input().rstrip().split())))
for x in range(4):
    for y in range(4):
        s.append(a[x][y]+a[x][y+1]+a[x][y+2]+a[x+1][y+1]+a[x+2][y]+a[x+2][y+1]+a[x+2][y+2])
print(max(s))
