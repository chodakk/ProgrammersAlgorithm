def solution(n):
    if n<3:
        return n
    
    step = [0]*(n+1)
    step[1] = 1
    step[2] = 2

    for i in range(3, n+1) :
        step[i] = step[i-1]+step[i-2]

    return step[n]%1234567


print(solution(4))