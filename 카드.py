from collections import deque

n = int(input())
deque = deque()

for i in range(n):
    deque.append(i + 1)

while len(deque) > 1:
    deque.popleft()
    move_num = deque.popleft()
    deque.append(move_num)

print(deque[0])

