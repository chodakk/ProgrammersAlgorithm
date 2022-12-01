def solution(n):
    answer = 0
    print(longJump(5, 0))
    return answer

def longJump(n,a):
    if n==1 :
        return a+1
    else :
        return longJump(n-1, a+1)

print(solution(4))