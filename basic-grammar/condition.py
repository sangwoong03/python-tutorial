# if 조건문
# if 조건1 :
#   조건1이 참일 때 실행할 코드
# elif 조건2 :
#   조건2가 참일 때 실행할 코드

print("================================ Condition wtih Var ================================")

a = 14
if (a < 10 and a > 7):
    print("a는 7보다 큽니다.")
elif (a < 7 and a > 3):
    print("a는 7보다 작고 3보다 큽니다.")
elif (a > 10 or a == 0):
    print("a의 범위를 재설정해주세요.")

print("================================ Condition wtih List ================================")

number = [1, 3, 5, 7, 9]
check_number = 6
if check_number in number:
    print("Yes!!!")
else:
    print("Nop!!!")
