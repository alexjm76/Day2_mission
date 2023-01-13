import random

secret = random.randint(1,10)

guess = int(input("숫자 1~10까지 한 숫자를 입력해 주세요 : "))

if guess < secret:
    print("too low")
elif guess > secret:
    print("too high")
else:
    print("just right")

print(f"숫자는 {secret}였습니다")