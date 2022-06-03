# 주어진 리스트안에 있는 단어 중
# 가장 긴 단어를 찾을수 있도록 함수를 완성해주세요.
# ["PHP", "Exercises", "Backend"] --> "Exercises"

def find_longest_word(words):
    # 아래 코드를 작성해주세요.
    min_len = 0
    longest_word = ""

    for i in range(len(words)):

        if len(words[i]) > min_len:

            min_len = len(words[i])
            longest_word = words[i]

        else:
            longest_word = words[i-1]

    return longest_word
