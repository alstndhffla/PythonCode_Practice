"""
각 자리 숫자의 합을 구하라
리스트와 map() 함수를 이용
"""


def sumOfDigits(num):
    digits = map(int, list(str(num)))
    return sum(digits)


if __name__ == '__main__':
    print(sumOfDigits(47253))
    print(sumOfDigits(643))