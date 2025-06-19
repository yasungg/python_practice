# 카페



# set으로 선언
menu = {"아메리카노", "라떼", "녹차"}
print(menu)

menu = list(menu)
print(menu, type(menu))

menu = tuple(menu)
print(menu, type(menu))

menu = set(menu)
print(menu, type(menu))

from random import *

list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
print(list)

shuffle(list)
print(list)
congrat = sample(list, 4)

print(congrat)
print(" -- 당첨자 발표 -- ")
print("치킨 당첨자 : {0}".format(congrat[0]))
print("커피 당첨자 : {0}".format(congrat[1:]))

print("치킨 당첨자 : %d" %congrat[0])
print("커피 당첨자 : %d, %d, %d" %(congrat[1], congrat[2], congrat[3]))
print(" -- 축하합니다 -- ")
