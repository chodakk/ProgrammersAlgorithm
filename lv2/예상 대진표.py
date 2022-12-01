import math

def solution(n,a,b):
    answer = 0
    newA = a
    newB = b

    while newA!=newB :
        answer += 1
        newA = (newA+1)//2
        newB = (newB+1)//2

    return answer

print(solution(8,4,7))