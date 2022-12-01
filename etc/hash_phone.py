def solution(phone_book):
    answer = True
    phone_book = sorted(phone_book)
    
    for be, af in zip(phone_book, phone_book[1:]):
        if af.startswith(be):
            answer = False

    return answer

print(solution(["119", "97674223", "1195524421"]))