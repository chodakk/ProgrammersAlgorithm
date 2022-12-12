def solution(n, s):
    answer = []

    if s//n == 0:
        return [0,0]
    
    while n >= 1:
        answer.append(s//n)
        s -= s//n
        n -= 1

    return answer

print(solution(2, 9))