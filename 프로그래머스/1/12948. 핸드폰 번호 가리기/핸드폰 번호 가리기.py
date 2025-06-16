def solution(phone_number):
    num = len(phone_number)
    result = '*' * (num-4) + phone_number[num-4:]
    return result