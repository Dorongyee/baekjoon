def custom_key(x):
    # 문자열을 4번 반복하여 길게 만들고 비교
        return x * 5

def solution(numbers):
    # 문자열로 변경, 내림차순으로 변경후 전부 연결해서 출력 (O(NlogN))
    str_numbers = list(map(str, numbers))
    # custom_key를 이용하여 정렬
    sorted_numbers = sorted(str_numbers, key=custom_key, reverse=True)
    if sorted_numbers[0] == "0":
        return "0"
    result = ''.join(sorted_numbers)
    return result