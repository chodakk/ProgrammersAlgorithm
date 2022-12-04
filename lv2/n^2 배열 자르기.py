def solution(n, left, right):
    answer = []

    for i in range(left+1, right+2) :
        quotient = i//n
        remainder = i%n
        
        if remainder==0 :
            answer.append(n)
        else :
            answer.append(max(quotient+1, remainder))

    return answer

print(solution(3,2,5))