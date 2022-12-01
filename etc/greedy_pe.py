def solution(n, lost, reserve):
    lost.sort()
    reserve.sort()

    lostC = lost.copy()

    for l in lost :
        if l in reserve :
            lostC.remove(l)
            reserve.remove(l)
            
    lost = lostC
    answer = n-len(lost)

    for l in lost :
        print(reserve)
        if l-1 in reserve :
            reserve.remove(l-1)
            answer += 1
        elif l+1 in reserve : 
            reserve.remove(l+1)
            answer += 1
    
    return answer

print(solution(5, [1,2,4], [2,3,4,5]))