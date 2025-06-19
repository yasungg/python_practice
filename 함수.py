def open_account():
    print("새로운 계좌가 생성되었습니다.")


def deposit(balance, money):
    print("입금이 완료되었습니다. 남은 잔액은 {0}원입니다.".format(balance + money))
    return balance + money

def withdraw(balance, money): #출금
    if balance > money:
        print("출출금이 완료되었습니다. 남은 잔액은 {0}원입니다.".format(balance - money))
        return balance - money
    elif balance < money:
        print("잔액이 부족합니다. 고객님의 잔액은 {0}원입니다.".format(balance))
        return balance


balance = 0
balance = deposit(balance, 1000)
print(balance)

balance = withdraw(balance, 1100)
print(balance)

# 함수 기본값 설정
# age처럼 기본값을 설정해두면 변수를 따로 전달받지 않으면 기본값 출력, 변수 받으면 그걸로
# 다만, 기본값이 설정된 변수는 매개변수들 중 가장 뒤에 작성해야 한다. syntax error!!
# SyntaxError: parameter without a default follows parameter with a default

def profile(name, main_lang, age=20): 
    print("이름 : {0}\n주 사용 언어 : {1}\n나이 : {2}" \
          .format(name, main_lang, age))

profile("유지민", "python", 20)
profile("김민정", "java", 24)

# 변수 이름을 직접 작성해 함수를 호출하면 순서가 바귀어도 맞춰서 적용된다.
profile(main_lang="C#", name="아린", age=26)

# 가변인자
# 같은 함수를 사용하는데, 같은 카테고리 내에서 입력해야 하는 변수가 다를 때
# 예를 들면 할 줄 아는 언어의 개수가 다른 두 입사 지원자


def profilee(name, age, *language):
    print(f"이름 : {name}, 나이 : {age}\t", end=" ")
    for lan in language:
        print(lan, end=" ")
    print()

profilee("닝닝", 20, "Kotlin", "Swift")

gun = 10

def checkpoint(soldiers): #경계근무
    # 기본적으로 함수 내에서 전역변수는 적용되지 않는다.
    global gun # 전역 변수로 선언된 변수를 이 함수 내에서 사용하겠다는 뜻
    gun = gun - soldiers
    print(f"[함수 내] 남은 총 : {gun}")

checkpoint(2)

# Quiz 표준 체중 구하는 프로그램 작성

# 성별 공식
# 남자 : 키(m) * 키 (m) * 22
# 여자 : 키(m) * 키 (m) * 21

# 조건1 : 표준 체중은 별도의 함수 내에서 계산
#       * 함수명 : std_weight
#       * 전달값 : height, gender
# 조건2 : 표준 체중은 소수점 둘째 자리까지 표시

#(출력 예제) 키 175cm 남자의 표준 체중은 67.38kg입니다.

def std_weight(height, gender):
    weight = ""
    height = height / 100
    if gender == "남자":
        weight = str(height * height * 22)[:5]
    elif gender == "여자":
        weight = str(height * height * 21)[:5]
    
    print(f"키{height}m {gender}의 표준 체중은 {weight}kg입니다.")


std_weight(173, "남자")
std_weight(168, "여자")