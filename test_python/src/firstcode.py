import random

computer_number = random.randint(1, 100)
while True:
    person_number = int(input("请输入一个数字:"))
    if person_number > computer_number:
        print("小一点")
    elif person_number < computer_number:
        print("大一点")
    elif person_number == computer_number:
        print("猜对了")
        break