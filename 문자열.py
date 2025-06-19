print('풍선')

#문자열에 곱셈 연산을 집어넣어서 반복시키는 것도 가능하다
print("ㅋ"*9)

jumin = "941026-1403712"

print("성별 : " + jumin[7])
print("출생연도 : " + jumin[0:2]) # 0번째부터 n번째 직전까지의 값을 가져옴 ex 0:2 = 0,1
print("출생월 : " + jumin[2:4])
print("출생일 : " + jumin[4:6])

print("생년월일 : " + jumin[:6]) # 앞에 숫자 없으면 처음부터
print("뒤 7자리 : " + jumin[7:]) #뒤에 숫자 없으면 뒤에 끝까지

print("뒤 7자리(뒤에서부터 세어서) : " + jumin[-7:]) # 맨 뒤에서 7번째부터 끝까지

#문자열 처리 함수

python = "Python is Amazing"
print(python.lower())
print(python.upper())
print(python[0].isupper())
print(len(python)) # 전체 문자열의 길이 반환
print(python.replace("Python", "Java"))

index = python.index("n")
print(index)
index = python.index("n", index + 1)
print(index)

print(python.find("n"))

#find와 index의 차이
print(python.find("Java")) # -1을 반환
# print(python.index("Java")) # 찾는 값이 없으므로 그냥 error 내버림

print(python.count("n")) # 문장 내에서 특정 값이 총 몇 번 등장하는지 세어줌

#문자열의 포맷

#case1
print("나는 %d살 입니다." %20) #정수값을 임의로 설정하여 집어넣을 수 있음.
print("나는 %s을 좋아해요" %"파이썬") #문자열을 임의로 집어넣을 수 있음
print("Apple은 %c로 시작해요." %"A") #char, 문자 하나만
print("나는 %s색과 %s색을 좋아해요" %("검정", "파란")) #문자열 여러개
print("나는 %d개의 사탕과 %d개의 초코파이를 먹기를 원합니다." %(3, 4)) #숫자도 가능

#case2
print("나는 {}살입니다.".format(32))
print("나는 {}색과 {}색을 좋아해요".format("검정", "파란"))
print("나는 {0}색과 {1}색을 좋아해요".format("검정", "파란"))
print("나는 {1}색과 {0}색을 좋아해요".format("검정", "파란"))

#case3
print("나는 {age}살이며, {color}색을 좋아해요.".format(age = 20, color = "검정"))

#case4(version 3.6 이상부터)
age = 20
color = "검정"
print(f"나는 {age}살이며, {color}색을 좋아해요.")

#탈출문자

#\n 문장 내 줄바꿈
print("백문이 불여일견\n백견이 불여일타")

#따옴표
#print("나는 "곽용석"입니다.")를 쓰고 싶다면
#case1 -> 따옴표 교차해서
print('나는 "곽용석"입니다.')
#case2 -> 역슬러시
print("나는 \"곽용석\"입니다.")

# 같은 원리로, \\를 입력하면 문장 내에서는 하나의 \로 바뀌어서 나오게 됨\

# \r : 뒤에 나오는 문자열을 문장의 맨 앞으로 이동(기입력된 문자열을 삭제하고 입력된다)
print("Red Apple\rPine")

# \b : 백스페이스 (한글자 삭제)
print("Redd\b Apple")

# \t : tab
print("Red\tApple")

# Quiz

email = "http://naver.com"

password = email[7:10] + str(len(email[7:12])) + str(email.count("e")) + "!"
print(password)

#정답은 replace와 index를 이용해서 먼저 문자열을 같은 기준으로 편집하는 과정을 먼저 거침
