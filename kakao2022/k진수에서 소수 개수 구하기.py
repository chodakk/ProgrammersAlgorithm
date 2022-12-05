def solution(n, k):
    answer = 0
    conv = ""
    
    while n!=0 :
        conv += str(n%k)
        n = n//k

    conv = conv[::-1]
    convSplit = conv.split("0")
    
    for convs in convSplit :
        if convs.isnumeric() :
            convs = int(convs)
            if is_prime(convs) :
                answer += 1

    return answer

def is_prime(n) :
    if n<2 : return False
    for i in range(2, int(n**0.5)+1) :
        if n%i == 0 :
            return False
    return True

print(solution(110011, 10))