def solution(elements):
    eleSet = set()

    length = len(elements)
    elements = elements*2 #2개 이어붙이기

    for i in range(length):
        for j in range(length):
            eleSet.add(sum(elements[i:i+j+1]))
    print(eleSet)
    return len(eleSet)

print(solution([7,9,1,1,4]))