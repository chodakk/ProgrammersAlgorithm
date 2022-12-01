def solution(s):
    answer = ''
    splitS = s.split(" ")
    print(splitS)

    for sS in splitS :
        if sS=='' :
            answer += " "
        else: 
            sS = sS.lower()
            wordsS = sS[0].upper() + sS[1:]
            answer += wordsS + " "

    return answer[:-1]

print(solution("3people  unFollowed me"))