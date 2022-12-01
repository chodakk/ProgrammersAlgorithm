def solution(sizes):
    list1 = []
    list2 = []
    for s in sizes :
        w = s[0]
        h = s[1]
        if(w>h) :
            list1.append(w)
            list2.append(h)
        else : 
            list1.append(h)
            list2.append(w)

    return max(list1)*max(list2)

print(solution([[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]))