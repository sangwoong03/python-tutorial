# 2개의 리스트를 input으로 받습니다.
# input 받은 2개의 리스트를 하나의 리스트로 합칩니다.
# 합쳐진 리스트의 첫 element와 마지막 element를 서로 바꾼 후 리스트 전체를 리턴 합니다.
# input 모두 빈 리스트이면 빈 리스트를 리턴합니다.

def merge_and_swap(list1, list2):
    # 모두 빈 리스트인 경우
    if (list1 == [] and list2 == []):
        return []
    # 빈리스트가 없거나, 하나만 빈 리스트인 경우
    else:
        list1 = list1 + list2

        # 하나만 빈 리스트인 경우 아래 로직을 수행하지 못해 indexError가 발생한다.
        first_value = list1[0]
        last_value = list1[-1]

        list1[0] = last_value
        list1[-1] = first_value

        return list1


list1 = [1, 2, 3, 4, 5]
list2 = [6, 7]

print(merge_and_swap(list1, list2))
