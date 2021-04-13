"""
재귀적 호출을 사용하지 않은 코드
"""


def sumOfDigits(num):
    sum = 0

    while num >= 1:
        sum = sum + (num % 10)
        num = num // 10

    return sum


if __name__ == '__main__':
    print(sumOfDigits(47253))
    print(sumOfDigits(643))