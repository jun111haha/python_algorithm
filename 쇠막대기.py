range_list = list(input())
stack = []
answer = 0

for i in range(len(range_list)):
    if range_list[i] == '(':
        stack.append('(')
    else:
        stack.pop()
        if range_list[i - 1] == '(':
            answer += len(stack)
        else:
            answer += 1

print(answer)
