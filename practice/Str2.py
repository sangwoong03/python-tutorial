# 문자열의 첫번째 문자는 인덱스 값 0 을 가집니다.
# 만약 문자열에 해당 문자가 여러번 나타나면, 첫번째로 나타나는 위치를 반환해야 합니다.
# 만약 문자가 문자열에 존재하지 않는다면, -1 을 반환해야 합니다.
# find 함수를 사용하지 마세요.
# 예시)
# ('a', 'I am a hacker') --> 2

def get_find(char, str):
    # 아래 코드를 작성해주세요.
    result = -1

    for i in range(len(str)):
        if(char == str[i]):
            result = i
            break

    return result


print(get_find('a', 'I am a hacker'))
