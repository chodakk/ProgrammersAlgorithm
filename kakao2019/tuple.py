def solution(s):
    answer = []

    divide1 = sorted(s[2:-2].split("},{"), key=len)

    for i in divide1:
        divide2 = list(map(int, i.split(",")))
        for j in divide2 :
            if(j not in answer):
                answer.append(int(j))

    return answer

print(solution("{{4,2,3},{3},{2,3,4,1},{2,3}}"))