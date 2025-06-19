print("대기번호 : 1")
print("대기번호 : 2")
print("대기번호 : 3")
print("대기번호 : 4")

for waiting_no in [0,1,2,3,4]:
    print("대기번호 : {0}".format(waiting_no+1))

for waiting_no in range(1, 6):
    print("대기번호 : {0}".format(waiting_no))


starbucks = ["유지민", "김민정", "아린"]

for customer in starbucks:
    print("{0} 고객님, 커피 준비되었습니다.".format(customer))

# while문

customer = "유지민"
index = 5

while index >= 1:
    print("{0} 고객님, 커피 준비되었습니다. {1}번 남았어요.".format(customer, index))
    index -= 1
    if index == 0:
        print("{0} 고객님의 커피가 폐기처분되었습니다.".format(customer))

absent = [2, 5]
no_book = [9]

# continue와 break
for student in range(1, 11):
    if student in absent:
        continue

    if student in no_book:
        print("{0} 너는 앞으로 나와 이 새꺄".format(student))
        break
    
    print("{0}번이 책을 읽어줘".format(student))

# 한 줄로 끝내는 for 문
# 출석번호가 1,2,3,4 앞에 100을 붙이기로 함 -> 101, 102, 103, 104

students = [1, 2, 3, 4, 5]

students = [i + 100 for i in students]
print(students)

# 영웅들 이름을 길이로 변환

heroes = ["Thor", "IronMan", "Starlord"]

# heroes = [len(name) for name in heroes]
# print(heroes)

# 영웅들 이름을 대문자로 변환

heroes = [name.upper() for name in heroes]
print(heroes)


# Quiz

# 50명의 승객과 매칭될 기회, 총 탑승 승객 수를 구하시오.
# 조건 1: 승객별 운행 소요 시간은 5~50분 사이의 난수로 정해진다.
# 조건 2: 당신은 소요 시간 5~15분 사이의 승객만 매칭해야 한다.

# 출력 예제
# [0] 1번째 손님 (소요시간 :15분)
# [0] 2번째 손님 (소요시간 :50분) ...

# 총 탑승 승객 : 2분

from random import *
passenger = 0
time = 0

for caller in range(1, 51):
    time = int(random() * 50 + 5)

    if time >= 5 and time <= 15:
        passenger += 1
        continue
    print("[0] {0}번째 손님 (소요시간 : {1}분)".format(caller, time))

print("총 탑승 승객 : {0}".format(passenger))