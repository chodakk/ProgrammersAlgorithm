def solution(land):
    
    for i in range(1,len(land)):
        for j in range(4) :
            land[i][j] += max(land[i-1][k] for k in range(4) if k!=j)

    return max(land[-1])

print(solution([[1,2,3,5],[5,6,7,8],[4,3,2,1]]))