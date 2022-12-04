def solution(arr):
    answer = 0

    arr.sort(reverse = True)
    max = arr[0]
    arr = arr[1:]
    all0arr = [0] * len(arr)

    n = 0
    rest = []
    
    while all0arr != rest :
        n+=1
        num = n*max
        rest = [num%a for a in arr]

    return n*max


print(solution([2,6,8,14]))