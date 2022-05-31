# Input으로 주어진 리스트에서 홀수는 전부 지우고 짝수만 남은 리스트를 리턴해주세요.
# 리스트의 요소들은 전부 숫자 값이고 총 요소 수는 5개 입니다.

def answer(nums):

    for num in nums[:]:
        if(num % 2 == 1):
            nums.remove(num)

    return nums


input = [
    [1, 2, 3, 4, 5],
    [1, 3, 9, 13, 5]
]

for i in range(len(input)):
    print(answer(input[i]))
