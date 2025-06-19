# 집합 (Set)
# 중복이 안됨, 순서가 없음
# 중괄호로 선언하되, key를 함께 적지 않으면 set의 선언
my_set = {1,2,3,3,3}
print(my_set)

boob = {"유지민", "옐"}

# set을 선언할 때, 배열을 만들고 set()으로 감싸도 된다.
slender = set(["김민정", "아린"])

slave = {"유지민", "김민정", "옐", "아린"}
# 두 set에서 중복된 값을 가져올 경우
print(slave & slender)
# intersection 똑같이 교집합을 반환
print(slave.intersection(boob))

# 합집합, 순서가 없기 때문에 순서가 보장되지는 않음
print(boob | slender)
print(boob.union(slender))

# 차집합
print(slave - boob)
print(slave.difference(slender))

# set에 값을 추가
boob.add("지원")
print(boob)

# 값을 제거
boob.remove("지원")

