print("================================ def function ================================")

people = [0, 1, 1, 0, 1, 1, 0]


def Hello(arr):
    for i in arr:
        if arr[i] == 0:
            print("초멘나사이")
        else:
            print("또 오셨슈~")


Hello(people)
