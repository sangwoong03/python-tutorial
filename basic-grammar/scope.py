# scope의 이해
# 중첩함수, closure와 같이 이해하면 좋은 부분
# Built in > Module > Enclosing > Local

what_is_my_scope = 11  # Global Scope


def scope_test(what_is_my_scope):

    what_is_my_scope = 12  # Enclosing Scope

    multiplier = 9

    def inner_scope_test(what_is_my_scope):

        what_is_my_scope = 7  # Loacl Scope

        return what_is_my_scope * multiplier

    return inner_scope_test(what_is_my_scope)


print(scope_test(10))  # 63
print(scope_test(20))  # 63
print(scope_test(333))  # 63
