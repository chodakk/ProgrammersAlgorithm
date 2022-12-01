def solution(s):
    conv = 0
    delete0 = 0
    sdelete0 = s.replace("0", "")

    while s != "1" :
        conv += 1
        delete0 += len(s) - len(sdelete0)
        s = str(bin(len(sdelete0))[2:])
        sdelete0 = s.replace("0", "")
        
    return [conv, delete0]


print(solution("01110"))