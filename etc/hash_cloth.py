def solution(clothes):
    answer = 1
    clothDict = {}

    for cloth in clothes :
        sorting = cloth[1]
        if sorting not in clothDict : 
            clothDict[sorting] = 1
        else :
            clothDict[sorting] = clothDict[sorting]+1

    for value in clothDict.values() :
        answer *= (value+1)

    return answer-1

print(solution([["a", "headgear"], ["b", "headgear"], ["c", "eyewear"], ["d", "eyewear"], ["e", "face"], ["f", "face"]]))