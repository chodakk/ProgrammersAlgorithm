def solution(n, words):
    answer = [0, 0]
    start = words[0][0]
    turn = 0
    wordList = []

    for idx,word in enumerate(words) :

        turn += 1
        if turn > n :
            turn -= n

        if (not word.startswith(start)) or (word in wordList) :
            answer = [turn, (idx//n)+1]
            break
        else :
            wordList.append(word)

        start = word[-1]
    
    return answer


print(solution(2, ["hello", "one", "even", "never", "now", "world", "draw"]))