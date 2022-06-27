import re

data = """
    	sang 961206-1234567
        woong 960216-2134657
 """
# ==================================== with Regular Expression ====================================
pat = re.compile("(\d{6})[-](\d{7})")
print(pat.sub("\g<1>-*******", data))


# ==================================== without Regular Expression ====================================
# def condition():
#     result = []

#     for line in data.split("\n"):
#         word_result = []
#         for word in line.split(" "):
#             if len(word) == 14 and word[:6].isdigit() and word[7:].isdigit():
#                 word = word[:6] + "-" + "*******"
#             word_result.append(word)
#         result.append(" ".join(word_result))

#     print("\n".join(result))

# condition()

# ==================================== Regular Expression Exercise ====================================

# 영소문자숫자
# account = "^[a-z0-9+_.]{4,}"

# @포함 .포함 이메일 주소
# email = "^[a-zA-Z0-9+_.]+@[a-zA-Z0-9-]+.[a-zA-Z]{2,3}$"

# 11~12 숫자
# phone_number = "^[0-9]{10,11}$"

# 최소 8자 + 최소 한개의 영문자 + 최소 한개의 숫자
# password = "^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$"
