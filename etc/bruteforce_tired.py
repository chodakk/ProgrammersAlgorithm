from itertools import permutations

def solution(k, dungeons):
    answer = -1
    orders = list(permutations([i for i in range(len(dungeons))], len(dungeons)))
    
    for order in orders : 
        hp = k
        tempAns = 0
        for o in order :
            if hp >= dungeons[o][0] :
                hp -= dungeons[o][1]
                tempAns += 1
            else :
                break
        answer = max(answer, tempAns)
    
    return answer

print(solution(80, [[80,20],[50,40],[30,10]]))