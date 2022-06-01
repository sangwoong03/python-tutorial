# Input 으로 주어진 리스트에서 오직 한번만 나타나는 값 (unique value)을 가지고 있는 요소는 출력하기

# 다음과 같은 리스트가 주어졌다면:
# [1, 2, 3, 4, 5, 1, 2, 3, 7, 9, 9, 7]
# 다음과 같이 출력:
# 4
# 5

def answer(numbers):
    new_dic = {}

    for number in numbers:
        if number in new_dic:
            new_dic[number] += 1
        else:
            new_dic[number] = 1

    for key in new_dic:
        if (new_dic[key] == 1):
            print(key)


input = [1, 2, 3, 4, 5, 1, 2, 3, 7, 9, 9, 7]

answer(input)
