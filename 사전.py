# Java의 HaashMap과 비슷한 자료구조, 키/값 쌍으로 구성됨.

slave = {1:"유지민", 2:"김민정"}

# 순서가 아니라 키값을 호출한다
print(slave)
print(slave[1])
print(slave.get(2))

#대괄호를 이용해 호출하면 호출 부호가 없을 경우 KeyError를 반환하며 종료
#get을 통해 호출하면 None을 반환하며 종료

#get을 통해 호출 후 호출 부호에 값이 없으면 뒤에 설정한 문자열 반환
print(slave.get(3, "공석"))

# 사전 자료형으로 구성된 배열에 특정 key가 있는지 확인하
print(2 in slave) # True 

# key는 문자열도 될 수 있음.
slave["빨통녀-1"] = "옐"
print(slave)

# 값 삭제 
del slave["빨통녀-1"]
print(slave)

# key들만 출력
print(slave.keys())

# value들만 출력
print(slave.values())

# key, value 쌍으로 출력
print(slave.items())

# 모든 값 다 지우기
slave.clear()
print(slave)