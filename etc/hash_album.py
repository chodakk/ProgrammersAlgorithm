def solution(genres, plays):
    answer = []

    dic1 = {} #장르 : (번호, 횟수)
    dic2 = {} #장르 별 횟수 합계

    for i, (g, p) in enumerate(zip(genres, plays)):
        if g not in dic1:
            dic1[g] = [(i, p)]
        else:
            dic1[g].append((i, p))

        if g not in dic2:
            dic2[g] = p
        else:
            dic2[g] += p
    
    print(dic1)

    for (k, v) in sorted(dic2.items(), key=lambda x:x[1], reverse=True): #횟수가 많은것부터 조회
        for (i, p) in sorted(dic1[k], key=lambda x:x[1], reverse=True)[:2]: #해당하는 장르를 조회하여 내림차순 -> 상위 2개만
            answer.append(i)

    return answer


print(solution(["A", "B", "A", "B", "A", "C"], [500, 600, 150, 800, 2500, 5000]))