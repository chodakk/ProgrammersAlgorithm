def solution(array, commands):
    answer = []

    for c in commands :
        i = c[0]
        j = c[1]
        k = c[2]
        tempArr = sorted(array[i-1:j])
        answer.append(tempArr[k-1])
    return answer

print(solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]))
