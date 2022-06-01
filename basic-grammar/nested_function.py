# 중첩 함수라
# 중첩 함수는 상위 부모 함수 안에서만 호출이 가능하다. 부모 함수 밖의 범위를 벗어나면 호출할 수 없다.
# 사용하는 이유는 가독성과 closure 때문이다.
# 1. 반복되는 코드 블럭을 함수로 정의하여 효과적으로 코드를 관리하고 가독성을 높일 수 있다.
# 2. closure를 통해 부모 함수가 외부 변수로부터 접근을 격리하고, 중첩함수를 통해서 부모함수의 변수를 사용한 연산은 가능하게 해준다.

# Decorator 구현하기

def decorator(func):
    result = "쉼표 뒷 부분이 꾸며주는 부분"

    def wrapper():

        return func() + result
    return wrapper


@decorator
def func1():
    return "여기가 꾸밈을 받는 부분이고, "


print("================== decorator 사용 ==================")
print(func1())


# Decorator를 사용하지 않는 방법은

def without_deco(func):
    result = "데코레이터를 쓰지 않는 함수입니다."
    return func() + result


def func2():
    return "그냥 이어붙이는 연습, "


print("================== decorator 미사용 ==================")
print(without_deco(func2))
