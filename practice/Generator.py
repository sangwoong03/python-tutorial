# Generator
# 함수의 return은 값을 반환하고 함수를 종료한다.
# 하지만 generator는 함수의 값을 산출한다는 것에 차이점이 있다.
# Iterator를 생성해주는 함수라고 볼 수 있다.
# 그렇기 때문에 적은 메모리의 크기를 가질 수 있습니다.

import time

# 사용 예제


def generator_squares():
    for i in range(3):
        yield i ** 2


gen = generator_squares()

# generator는 __iter__와 __next__함수가 둘 다 들어있다.
# 따로 __next__ 함수를 호출하지 않아도 바로 사용할 수 있다.
# Interator와 마찬가지로 값을 반환한 그 지점에서 다시 호출을 할 수 있다.
print(generator_squares())
print("==============기본 사용 예시==============")
print(gen.__next__())
print(gen.__next__())
print(gen.__next__())


# generator에 들어있는 send 함수로 값을 전달하는 예제
def generator_send():
    received_value = 0

    while True:

        received_value = yield
        print("received_value = ", end=""), print(received_value)
        yield received_value * 2


gen_1 = generator_send()
next(gen_1)

print("==============send 함수로 값을 전달하는 예제==============")
print(gen_1.send(2))


# Generator 표현식
L = [1, 2, 3]


def generate_square_from_list():
    result = (x*x for x in L)  # 튜플 컴프리헨션이지만 제너레이터가 나옴. tuple() 감싸야 튜플 컴프리헨션
    print(result)
    return result


def print_iter(iter):
    for element in iter:
        print(element)


print("==============표현식 예제==============")
print(generate_square_from_list())
print_iter(generate_square_from_list())


# 코드 분석 예제


def print_iter_1(iter):
    for element in iter:
        print(element)


def lazy_return(num):
    print("sleep 1s")
    time.sleep(1)  # 일시정지 함수
    return num


print("comprehension_list=")
# 배열 값이 한번에 만들어지고 함수가 끝나면 값을 반한함.
comprehension_list = [lazy_return(i) for i in L]
print_iter_1(comprehension_list)

print("generator_exp=")
# 튜플의 값이 함수가 실행될 때마다 하나씩 만들어지고 하나씩 반환함.
generator_exp = (lazy_return(i) for i in L)
print_iter_1(generator_exp)
