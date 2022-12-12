def solution(elements):
    eleSet = set()

    length = len(elements)
    elements = elements*2 #2개 이어붙이기

    for i in range(length): #앞에서부터 하나씩 이동
        for j in range(length): #몇개 묶을 것인지
            eleSet.add(sum(elements[i:i+j+1]))
    
    return len(eleSet)

print(solution([7,9,1,1,4]))