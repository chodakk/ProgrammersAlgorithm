def solution(brackets):
    answer = True
    open = []

    for b in brackets :
        try :
            if b=="(" : open.append(b)
            else : open.pop(0)
        except :
            return False

    if len(open)==0 : return True
    else : return False


print(solution("(()("))