# Lambda Expression

# import types


# def f(x, y, z): return x+y+z


# print(f)
# print(type(f))
# print(type(f) == types.LambdaType)

# types_number = (len([i for i in dir(types) if not i.startswith("__")]))
# types_kind = dir(types)
# print(f"types 모듈은 총 {types_number}개이고 {types_kind}가 있습니다.")


# 다음 함수를 람다표현식을 사용하여 작성해보기
def check_password(password):
    if len(password) < 8:
        return 'SHORT_PASSWORD'
    if not any(c.isupper() for c in password):
        return 'NO_CAPITAL_LETTER_PASSWORD'
    return True


# 람다표현식과 람다표현식 사이에는 쉼표로 구분을 해주어야함.
# if 구문과 같이 사용할 경우 else 구문도 함께 작성해주어야 함.
lambdas = [
    lambda x: "SHORT_PASSWORD" if len(x) < 8 else None,
    lambda x: "NO_CAPITAL_LETTER_PASSWORD" if not any(
        c.isupper() for c in x) else None
]


def check_password_using_lambda(password):

    for f in lambdas:
        if f(password) is not None:
            return f(password)

    return True


print(check_password_using_lambda('123'))            # SHORT_PASSWORD
# NO_CAPITAL_LETTER_PASSWORD
print(check_password_using_lambda('12356789f'))
print(check_password_using_lambda('123456789F'))    # True
