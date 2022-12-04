def solution(arr1, arr2):
    row = len(arr1)
    col = len(arr2[0])
    answer = [[0]*col for _ in range(row)]

    for i in range(0,row) :
        rowArr1 = arr1[i]
        for j in range(0, col) :
            value = 0
            for k in range(0, len(arr2)) :
                value += rowArr1[k] * arr2[k][j]
            answer[i][j] = value

    return answer

print(solution([[2, 3, 2], [4, 2, 4], [3, 1, 4]], [[5, 4, 3], [2, 4, 1], [3, 1, 1]]))