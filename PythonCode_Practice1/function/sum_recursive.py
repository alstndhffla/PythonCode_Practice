"""
어떤 수(number)의 각 자리 숫자(digit)의 합을 계산하는 sumOfDigits()라는 재귀 함수를 작성
입력한 수를 읽어 sumOfDigits() 함수를 호출하며,
이 함수는 합산할 숫자가 남지 않을 때까지 자신을 호출해,
최종적인 합을 사용자에게 표시
"""


def sumOfDigits(num):
    if num >= 1:
        return num % 10 + sumOfDigits(num // 10)
    else:
        return 0


if __name__ == '__main__':
    print(sumOfDigits(47253))
    print(sumOfDigits(643))
