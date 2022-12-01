def solution(s):
    answer = 0
    s = list(s)
    for i in range(len(s)) :
        s.append(s.pop(0))
        answer += isCorrect(s)

    return answer

def isCorrect(arr) :
    stack = []
    brackets = {"(":")", "{":"}", "[":"]"}
    
    for a in arr :
        if a in brackets :
            stack.append(brackets[a])
        else :
            if not stack:
                return 0
            br = stack.pop()
            if br != a :
                return 0
    return 1

print(solution("}]()[{"))
