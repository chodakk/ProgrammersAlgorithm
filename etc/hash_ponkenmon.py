def solution(nums):
    answer = 0
    numSet = set(nums)
    if len(numSet) < len(nums)/2 :
        answer = len(numSet)
    else :
        answer = len(nums)/2

    return int(answer)


print(solution([3,3,3,2,2,4]))
