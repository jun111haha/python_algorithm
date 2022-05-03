N , M = map(int,input().split())
a = set()
b = set()

for i in range(N):
    str = input()
    a.add(str)

for i in range(M):
    str = input()
    b.add(str)

arr = sorted(list(a & b))
print(len(arr))

for i in arr:
    print(i)