def solution(A,B):
    answer = 0
    A.sort()
    B.sort(reverse=True)
    
    for a,b in zip(A,B) :
        answer += a*b

    return answer


print(solution([1,2],[3,4]))