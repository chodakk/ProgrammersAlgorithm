import heapq

def solution(operations):
    heap = []

    for op in operations : 
        if op[0]=='I':
            heapq.heappush(heap, int(op[2:]))
        else:
            if len(heap)==0:
                continue
            elif op[2]=='1':
                heap = heapq.nlargest(len(heap), heap)[1:]
                heapq.heapify(heap)
            else :
                heapq.heappop(heap)

    if heap:
        return [heapq.nlargest(1, heap)[0], heapq.heappop(heap)]
    else :
        return [0,0]

print(solution(["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]))