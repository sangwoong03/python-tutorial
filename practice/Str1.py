# 문자열이 주어졌을 때 "-"를 기준으로 앞에 있는 문자열을 반환하시오
# 예시)
# 'BTC-KRW' --> BTC

# split
def get_prefix(str):
    # 아래 코드를 작성해주세요.
    new_str = str.split("-")
    first_new_str = new_str[0]

    return first_new_str


# for loop
# 차후 수정
