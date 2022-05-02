'''
중요도 리스트의 첫번째 값과 같다면 출력
위치리스트와 비교를통해 사용자가 궁금한값 도출
'''
testCase = int(input())

for i in range(testCase):
    N, M = map(int,input().split())

    printList = list(map(int,input().split()))
    checkList = [0 for i in range(N)] 
    checkList[M] = 1

    count=0
    while True:
        if printList[0] == max(printList):
            count+=1

            if checkList[0] != 1:
                del printList[0]
                del checkList[0]
            else:
                print(count)
                break
        else:
            printList.append(printList[0])
            checkList.append(checkList[0])
            del printList[0]
            del checkList[0]