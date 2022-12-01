def solution(arr):
    answer = []
    before = arr.pop(0)
    for a in arr :
        now = a
        if(before==now) : continue
        else : 
            answer.append(before)
            before = now
    answer.append(arr[-1])
    return answer


print(solution([1,1,3,3,0,1,0,1]))