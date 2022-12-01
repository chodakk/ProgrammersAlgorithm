def solution(s):
    answer = ''
    splitS = list(map(int, s.split(" ")))
    answer += str(min(splitS)) + " "
    answer += str(max(splitS))

    return answer

print(solution("1 2 3 4"))