# List []
# '순서를 따지는' 객체의 집합

# 지하철 칸별로 10명, 20명, 30명

# subway1 = 10
# subway2 = 20
# subway3 = 30

# subway = [10, 20, 30]
# print(subway)

subway = ["김민정", "안유진", "유지민"]

#안유진은 몇번째 칸에 타고 있는가?
print(subway.index("안유진") + 1)

# append = 리스트 맨 뒤에 추가
subway.append("장원영")
print(subway)

# insert = 임의의 순서에 끼워넣음, 기존 값은 삭제되지 않고 인덱스가 뒤로 한 칸씩 밀림
subway.insert(2, "옐")
print(subway)

# pop = 뒤에서 하나씩 삭제
print(subway.pop())
print(subway)

# count = 같은 값을 가진 것의 갯수가 몇 개 있는지 확인
subway.append("김민정")
print(subway.count("김민정"))
subway.pop()

# 배열 순서 정렬

num_list = [5,3,4,1,2,]
print(num_list)
num_list.sort()
print(num_list)

# 배열 순서 뒤집기
num_list.reverse()
print(num_list)

# 배열 전체 지우기
num_list.clear()
print(num_list)

# list는 다양한 자료형을 함께 사용할 수 있다.

mix_list = ["장원영", "b컵", 170, 48, True]
print(mix_list)

# 두 리스트를 하나의 리스트로 합치는 것도 가능. 뒤에서부터 append 형식으로 추가되는 형태
subway.extend(mix_list)
print(subway)