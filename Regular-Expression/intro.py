import re

data = """
    	sang 961206-1234567
        woong 960216-2134657
 """
# ====================================with Regular Expression====================================
pat = re.compile("(\d{6})[-](\d{7})")
print(pat.sub("\g<1>-*******", data))

# ====================================without Regular Expression====================================
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
