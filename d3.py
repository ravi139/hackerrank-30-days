n = int(input())
s = set(map(int, input().split()))
N = int(input())
s.pop()
s.remove(9)
s.discard(9)
s.discard(8)
s.remove(7)
s.pop()
s.discard(6)
s.remove(5)
s.pop()
s.discard(5)
print(sum(s))
