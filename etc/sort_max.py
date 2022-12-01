def solution(numbers):
    answer = ''
    strNum = []
    for n in numbers :
        strNum.append(str(n))
    
    strNum.sort(key = lambda x:x*3, reverse=True)
    answer = str(int(''.join(strNum)))

    return answer

print(solution([3, 30, 34, 5, 9]))