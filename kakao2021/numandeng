def solution(s):
    answer = ""
    engToNum = {"one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9", "zero":"0"}
    str = ""

    for i in s :
        if i.isdigit() :
            answer+=i
        else :
            str+=i
            if str in engToNum :
                answer+=engToNum[str]
                str=""

    return int(answer)



print(solution("one4seveneight"))