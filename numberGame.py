import random

number = random.randint(1, 100)
win = False

for chance in range(7):
    print(7-chance,"번의 기회가 남았습니다. ")
    answer = input("숫자 입력 : ")
    if answer == number:
        print("정답입니다!")
        win = True
        break
    elif answer > number:
        print("입력하신 수는 정답보다 작은 수 입니다.")
    else:
        print("입력하신 수는 정답보다 큰 수 입니다.")
    chance+=1
if win:
    print("당신이 이겼습니다.")
else:
    print("당신이 졌습니다. 정답은 ",number,"입니다.")