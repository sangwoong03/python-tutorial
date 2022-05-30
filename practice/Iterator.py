# Iterator
# 값을 차례대로 꺼낼 수 있는 객체
# 연속된 숫자가 아주 많은 경우 많은 메모리를 사용하기 때문에 성능에도 불리하다.
# 이터레이터만 생성하고 값이 필요한 시점이 되었을 때 값을 만드는 방식을 사용한다.
# 데이터 생성을 뒤로 미루는 것을 말하는데 이를 지연 평가라고 한다.

# 반복 가능한 객체인지 확인하는 방법
# print(dir(데이터를 담은 변수))
# __iter__가 있는지 확인 >> 있다면 사용 가능


# List Iterator
L = [1, 2, 3, 4]

# for loop
for num in L:
    print(f"List_for_iterator :: {num}")


# while loop
I = iter(L)  # == I = L.__iter__() 이터레이터를 변수에 저장

while True:
    try:
        num = next(I)  # I.__next__() 메소드를 통해 값을 하나씩 호출
    except StopIteration:
        break
    print(f"List_while_iterator :: {num}")


# Dictionary Iterator
D = {'a': 1, 'b': 2, 'c': 3}

# for loop
for key in D.keys():
    print(f"Dic_for_iterator :: {key}")

# while loop
I_2 = iter(D)
while True:
    try:
        key = next(I_2)
    except Exception as e:
        break
    print(f"Dic_while_iterator :: {key}")
