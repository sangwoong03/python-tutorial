# 출력 방법
print("================================ 출력 방법 ================================")
print("출력 내용을 담아주세요")


# 변수 선언 방법
# JS와 달리 변수 선언 코드가 없음
variables = "변수에 담을 자료를 적어주세요"
print("================================ 변수 사용 ================================")
print(variables)


# 글자 일부만 떼어내기
print("================================ 글자 인덱싱 ================================")
print(variables[0])
print(variables[1])


# 문자열과 변수 같이 사용하여 출력하기
print("================================ 문자열+변수 ================================")
print(variables + "aaaaaaaaaaaaa")
print(f"""변수1 = {variables}""")
print("변수2 = {}.".format(variables))
