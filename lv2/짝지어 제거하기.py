def solution(str):
    answer = -1
    sList = []

    for s in str :
        if sList :
            last = sList.pop()
        else :
            sList.append(s)
            continue

        if last!=s:
            sList.append(last)
            sList.append(s)

    if sList :
        return 0
    else :
        return 1

print(solution("baabaa"))