def solution(priorities, location):
    priorities = [(i, x) for i, x in enumerate(priorities)]
    tmp = 0

    while len(priorities)>1 :
        before = priorities.pop(0)
        maxpr = max(priorities, key=lambda p: p[1])
        if(maxpr[1] > before[1]) :
            priorities.append(before)
        else :
            tmp += 1
            if before[0] == location :
                return tmp
    return tmp+1


print(solution([3,3,4,2], 3))