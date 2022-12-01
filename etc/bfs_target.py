def solution(numbers, target):
    sup= [0]
    for i in numbers:
        sub = []
        for j in sup : 
            sub.append(j+i)
            sub.append(j-i)
        sup = sub
        print(sub)
    return sup.count(target)

print(solution([4,1,2,1], 4))