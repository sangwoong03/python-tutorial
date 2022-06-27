# 양수 N을 이진법으로 바꿨을 때, 연속으로 이어지는 0의 갯수가 가장 큰 값을 반환하는 프로그램을 작성해주세요.

# 예시입니다:
# input: 9
# output: 2
# 설명: 9의 이진수는 1001 입니다.
# 1과 1사이에 있는 0은 2 이므로, 2를 return

# input: 529
# output: 4
# 설명: 529의 이진수는 1000010001 입니다.
# 1과 1사이에 있는 연속된 0의 수는 4와 3입니다.
# 이 중 큰 값은 4이므로 4를 return

# first Answer
# Used bin() method of python
def asnwer(N):
    result = []
    count = 0

    bi_num = bin(N)[2:]

    for i in bi_num:
        if i == "1":
            result.append(count)
            count = 0
        else:
            count += 1

    return max(result)

# second Answer
# Used while loop with remainder divided into 2


def answer(N):
    bi_nums = []
    result = []
    count = 0

    while True:
        if N // 2 == 0:
            bi_nums.append(N % 2)
            break
        else:
            bi_nums.apppend(N % 2)
            N = N // 2

    for i in bi_nums[::-1]:
        if i == 1:
            result.append(count)
            count = 0
        else:
            count += 1

    return max(result)
