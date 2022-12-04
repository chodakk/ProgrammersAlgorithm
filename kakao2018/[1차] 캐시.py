def solution(cacheSize, cities):
    answer = 0
    cityList = []

    if cacheSize==0 :
        return len(cities)*5

    for c in cities :
        city = c.upper()
        
        if city in cityList : #LRU
            cityList.remove(city)
            cityList.append(city)
            answer+=1
        else :
            if len(cityList)==cacheSize :
                cityList.pop(0) #LRU
            cityList.append(city)
            answer+=5
    
    return answer

print(solution(3, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))