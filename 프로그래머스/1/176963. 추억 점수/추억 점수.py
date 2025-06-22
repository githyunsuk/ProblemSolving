def solution(name, yearning, photos):
    result = []
    for photo in photos:
        temp = 0
        for p in photo:
            if p in name:
                temp += yearning[name.index(p)]
        result.append(temp)
    return result
        