def solution(brown, yellow):
    total = brown + yellow
    for i in range(1, int(total/2)+1) :
        if total%i == 0 :
            rest = int(total/i)
            if rest < i : break
            else :
                if 2*(rest+i)-4 == brown :
                    return [rest, i]
            

print(solution(24,24))