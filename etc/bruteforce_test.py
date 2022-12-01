def solution(answers):
    answer = []

    a = [1, 2, 3, 4, 5] * 2000
    b = [2, 1, 2, 3, 2, 4, 2, 5] * 1250
    c = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * 1000
    ansList = [0,0,0]

    for i in range(len(answers)) :
        if(a[i] == answers[i]) : ansList[0] += 1
        if(b[i] == answers[i]) : ansList[1] += 1
        if(c[i] == answers[i]) : ansList[2] += 1
    
    answer = [idx+1 for idx,value in enumerate(ansList) if value==max(ansList)]

    return answer

print(solution([1,2,3,4,5]))