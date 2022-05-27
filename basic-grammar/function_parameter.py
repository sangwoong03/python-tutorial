# 함수 인자 사용
print("========================== 위치 인자 ==========================")


def add(a, b, c):
    return a + b + c


print(add(1, 2, 3))


print("========================== 위치 인자 *args==========================")


def smart_phones(name, *phones):
    print(f"name :: {name}")
    print(f"phones:: {phones}")


smart_phones("애플", "아이폰3", "아이폰4", "아이폰5", "아이폰6")


print("========================== 키워드 가변 인자 *kwargs==========================")


def smart_phones(name, **phones):
    print(f"name :: {name}")
    for key in phones:
        print(f"""key = {key}, value = {phones[key]}""")


smart_phones("핸드폰", 애플="아이폰", 삼성="갤럭시", 엘지="뭐있냐")
