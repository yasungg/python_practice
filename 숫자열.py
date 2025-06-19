#연산자 심화

print(2**3) # 8, 2를 3번 제곱
print(5%3) # 2 5를 3으로 나눈 값의 나머지
print(10//3) # 3 10을 3으로 나눈 값의 몫

print(3 == 3) # True, 앞과 뒤의 값이 같은지를 확인하는 연산자
print(4 == 2) # False
print(3 + 4 == 7) # True

print(1 != 3) # True, 앞 뒤가 같지 않음을 이야기함
print(not 1 != 3) # False
print((3 > 0) and (3 < 5)) # True, 둘이 동시에 만족하는 경우
print((3 > 0) & (3 < 5)) # True, and 와 &은 똑같이 사용할 수 있음

print ((3 > 0) or (3 > 5)) # True, or 둘 중에 하나만 참이어도 true
print((3 > 0) | (3 > 5)) # or는 | 로도 사용할 수 있음

#숫자처리함수

print(abs(-5)) # -5의 절댓값인 5
print(pow(4, 2)) # 4^2 = 16
print(4 ** 2) # 4^2 = 16
print(max(5, 12)) # 12
print(min(5, 12)) # 5
print(round(3.14)) # 3 round = 반올림
print(round(4.99)) # 5

from math import *
print(floor(4.99)) # 내림 4
print(ceil(3.14)) # 올림 4
print(sqrt(16)) # 제곱근 4

from random import *
print(random()) # 0.0~ 1.0 미만의 임의의 값을 생성

print(random() * 10) # 0.0 ~ 10.0 미만의 임의의 값을 생성
print(int(random() * 10)) # 0 ~ 10 사이의 임의의 정수
print(int(random() * 10)) # 0 ~ 10 사이의 임의의 정수
print(int(random() * 10)) # 0 ~ 10 사이의 임의의 정수


print(int(random() * 10) + 1) # 0 ~ 10 사이의 임의의 정수
print(int(random() * 10) + 1) # 0 ~ 10 사이의 임의의 정수
print(int(random() * 10) + 1) # 0 ~ 10 사이의 임의의 정수

print(int(random() * 45) + 1) # 로또 뽑기
print(int(random() * 45) + 1)
print(int(random() * 45) + 1)
print(int(random() * 45) + 1)
print(int(random() * 45) + 1)
print(int(random() * 45) + 1)

print(randrange(1, 46)) # 1부터 46 미만의 임의의 값 생성 즉, 위를 더 간단하게
print(randint(1, 45)) # 1 ~ 45 이하의 값을 생성

print("오프라인 스터디 모임 날짜는 매월", randint(4, 28), "일로 선정되었습니다.")