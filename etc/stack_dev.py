import math

def solution(progresses, speeds):
    answer = []
    days = []
    for idx, (pr, sp) in enumerate(zip(progresses, speeds)) :
        day = (100-pr)/sp
        days.append(math.ceil(day))
    
    before = days.pop(0)
    answer.append(1)
    for d in days :
        if(d > before) :
            answer.append(1)
            before = d
        else :
            answer[-1] += 1

    return answer

print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))