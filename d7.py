n = int(input())
arr = []
for i in range(0,n):
    arr.append(list(map(int, input().strip().split(" "))))
print(str(arr[n::-1]))
'''n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]
r = arr[::-1]

for i in range(0,n):
    print (str(r[i]),end=" ")'''
