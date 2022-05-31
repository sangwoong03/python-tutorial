# 주어진 parameter 값을 나눌 수 있는 1을 제외한 최소의 양의 정수를 return하여야 합니다.
# 예) 15를 넣으면 3이 반환됩니다.

def answer(num):
    # 공약수의 최솟값 설정
    common_divisor = 2
    int_arr = []

    # 2이상의 값이 1만큼 증가하면서 num까지 루프 순회
    # num을 common_divisor로 나눈 값이 0이면 공약수이므로 리스트에 원소 추가
    while common_divisor <= num:
        if (num % common_divisor == 0):
            int_arr.append(common_divisor)
        common_divisor += 1

    # 최솟값 구하기
    min_number = num
    # 리스트의 각 공약수를 순회
    # num보다 작은 수가 나오면 min_number에 대입
    for int_number in int_arr:
        if (min_number > int_number):
            min_number = int_number

    return min_number


input = [15, 18, 25, 49, 81]

for i in range(len(input)):
    print(answer(input[i]))
