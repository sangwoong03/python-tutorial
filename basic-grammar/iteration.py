# Itertation


# for loop
print("================================ For Loop ================================")
for i in range(0, 6):
    print(i)

date = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
for i in date:
    print(i)

# While loop
print("================================ while Loop ================================")
date = 25
while date < 30:
    date += 1
    print("{} 다음 달로 넘어갑니다.".format(date))
    if (date == 30):
        print("1일입니다.")
