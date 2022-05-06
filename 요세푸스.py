N , M = map(int,input().split())
arr = [i for i in range(1, N + 1)]
answer = []
num = M - 1

for i in range(N):
    if len(arr) > num:
        answer.append(arr.pop())
        num = M - 1
    elif len(arr) <= num:
        num = num % len(arr)
        answer.append(arr.pop(num))
        num += M - 1




    

        









