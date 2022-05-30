# 리스트 컴프리헨션은 새로운 리스트를 만들 때 사용할 수 있는 간단한 표현식이다.
# [표현식 for 원소 in 반복 가능한 객체 if문]
# 일반 for loop보다 성능이 우수하다
# 다만 상황에 따라 가독성을 고려하여 어떤 것을 사용할지 판단을 잘 하자

# 1.다음과 같은 도시목록의 리스트가 주어졌을때, 도시이름이 S로 시작하지 않는 도시만 리스트로 만들 때 리스트 컴프리헨션을 사용하여 함수를 작성해 보세요.
# cities = ["Tokyo", "Shanghai", "Jakarta", "Seoul", "Guangzhou", "Beijing", "Karachi", "Shenzhen", "Delhi" ]
# 2.다음과 같은 도시, 인구수가 튜플의 리스트로 주어졌을때, 키가 도시, 값이 인구수인 딕셔너리를 딕셔너리 컴프리헨션을 사용한 함수를 작성해 보세요.
# population_of_city = [
#     ("Tokyo", 36923000),
#     ("Shanghai", 34000000),
#     ("Jakarta", 30000000),
#     ("Seoul", 25514000),
#     ("Guangzhou", 25000000),
#     ("Beijing", 24900000),
#     ("Karachi", 24300000),
#     ("Shenzhen", 23300000),
#     ("Delhi", 21753486)
# ]

# List-comprehension
def first_answer():
    cities = ["Tokyo", "Shanghai", "Jakarta", "Seoul",
              "Guangzhou", "Beijing", "Karachi", "Shenzhen", "Delhi"]
    list_comprehension = [city for city in cities if city[0:1] != "S"]
    return list_comprehension

# Dictionary-comprehension


def second_answer():
    population_of_city = [
        ("Tokyo", 36923000),
        ("Shanghai", 34000000),
        ("Jakarta", 30000000),
        ("Seoul", 25514000),
        ("Guangzhou", 25000000),
        ("Beijing", 24900000),
        ("Karachi", 24300000),
        ("Shenzhen", 23300000),
        ("Delhi", 21753486)
    ]
    dictionary_comprehension = {
        city: population for city, population in population_of_city}

    return dictionary_comprehension


print(first_answer())
print(second_answer())
