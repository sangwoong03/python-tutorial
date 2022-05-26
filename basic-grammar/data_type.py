# List in python
about_me = ["sangwoong", 27, "Osan"]

print("================================ List ================================")
print(about_me)
print(about_me[0])
about_me[1] = 17
print(about_me[1])
print(about_me[2])

# Dictionary
about_me_detail = {"name": "sangwoong", "age": 27, "where": "Osan"}
print("================================ Dictionary ================================")
print(about_me_detail)
print(about_me_detail["name"])
about_me_detail["age"] = 17
print(about_me_detail["age"])
print(about_me_detail["where"])

# Tuple
my_body = (174, 73)
print("================================ Tuple ================================")
print(my_body)
print(my_body[0])
print(my_body[1])
# 튜플은 수정, 삭제, 추가할 수 없음
# 데이터나 딕셔너리로 변환을 하여 튜플을 새로운 값으로 바꾼다면 가능

# Set
lotto_number = {5, 13, 17, 27, 35, 45}
print("================================ Set ================================")
print(lotto_number)
# 중복을 허용하지 않는 세트
new_list = [1, 1, 1, 2, 3, 3, 3, 4, 5, 6]
new_set = set(new_list)
print(new_set)  # 중복되는 원소가 사라진 것을 확인할 수 있음.
