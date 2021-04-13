# 태어난 해를 네 자리 연도로 입력하면 나이를 반환하는 함수

from datetime import datetime
today = datetime.today()

print(today)


def korean_age(birth_year):
    from datetime import datetime
    today = datetime.today()
    return today.year - birth_year + 1


if __name__ == '__main__':
    print("korean_age(2000):", korean_age(2000))