# 디렉터리에 없는 파일을 열려고 시도하는 경우
#
# f = open('없는 파일','r')
#
# Traceback (most recent call last):
#   File "C:\Users\11027\PycharmProjects\pythonProject\A0328.py", line 2, in <module>
#     f = open('없는 파일','r')
#         ^^^^^^^^^^^^^^^^^
# FileNotFoundError: [Errno 2] No such file or directory: '없는 파일'

#######################################

# 0으로 나누는 경우
# 4 / 0
#
# Traceback (most recent call last):
#   File "C:\Users\11027\PycharmProjects\pythonProject\A0328.py", line 12, in <module>
#     4 / 0
#     ~~^~~
# ZeroDivisionError: division by zero
#
############################################
#
# 배열 오류
# ㅁ = [1, 2, 3]
# ㅁ[4]
# 
# Traceback (most recent call last):
#   File "C:\Users\11027\PycharmProjects\pythonProject\A0328.py", line 26, in <module>
#     ㅁ[4]
#     ~^^^
# IndexError: list index out of range
#
######################################3
#
# 오류 예외 처리 기법 
''' try, except 문 '''
# 기본적인 try, except 문 형식
# try:
#     x = int(input('나눌 숫자 입력'))
#     y = 10 / x
#     print(y)
# except:
#     print("예외발생")
#
#
# except에 예외 조건을 걸어 만드는 방식
# li = [1, 2, 3]
# try:
#     x, y = map(int, input('인덱스, 나눌 숫자 입력').split())
#     print((li[x] / y))
# except ZeroDivisionError:  # 0으로 나눈 경우 예외 처리
#     print("0으로 나눌 수 없다")
# except IndexError:  # 인덱스를 잘못 입력한 경우 예외 처리
#     print("잘못된 인덱스")
#
###########################################################
#
''' raise 사용하기 '''

# try:
#     x = int(input("2의 배수 입력 : "))
#     if x % 2 != 0:
#         raise Exception("2의 배수가 이니다.")
#     print(x)
# except Exception as e:
#     print("예외 발생", e)
#
# # 2의 배수 입력 : 1
# # 예외 발생 2의 배수가 이니다.
#
## 클래스로 바꿔서 만들어보기
# class E(Exception):  # 자식 클래스 ( 부모 클래스 )
#     def __init__(self):
#         super().__init__('2의 배수 아님')
#
# def a():
#     try:
#         x = int(input("2의 배수 입력 : "))
#         if x % 2 != 0:
#             raise E
#         print(x)
#     except Exception as e:
#         print("예외 발생", e)
#
# a()
## 2의 배수 입력 : 3
## 예외 발생 2의 배수 아님
########################################
''' datetime 모듈 '''
import datetime

print(datetime.date.today())

t = datetime.date(2023, 3, 28)
# timedelta 를 이용해 날짜를 변경할 수 있다.
# + 는 이후 , - 는 이전 날짜
t = t + datetime.timedelta(weeks=1)
t = t - datetime.timedelta(days=3)

# 오늘을 기준으로 크리스마스까지 D-day 구하기
a = datetime.date(2023, 12, 25)
a2 = datetime.date.today()
diff = a - a2
print("D-day", diff.days, "일")

import time
print(time.strftime("%Y/%m/%d/%H/%M"))  # 날짜 포메팅
a = datetime.datetime.now()
print(a.strftime("%Y/%m/%d/%H/%M"))

# 1. 1부터 30까지의 숫자 중 홀수를 각 라인 단위로 파일에 입력하는 프로그램을 작성해라. (파일의 이름은 odd.txt)
with open('odd.txt', 'w') as f:
    for i in range(1, 31):
        if i % 2 != 0:
            f.write(str(i))
            f.write(' ')
        else:
            pass

# 2.	리스트가 주어질때, 자신을 제외한 곱셈을 출력해라.
# [ex][a, b, c, d]   => [bcd, acd, abd,abc]
# ex) 입력: [1,2,3,4]   출력: [24, 12, 8, 6]

list_a = [1, 2, 3, 4]
list_b = list()
for i in range(len(list_a)):
    temp = 1
    for j in range(len(list_a)):
        if i != j:
            temp *= list_a[j]
    list_b.append(temp)
print(list_b)

# 클래스 Calculator 작성
class Calculator:
    def __init__(self, b):
        self.b = b

    def sum(self):
        sum = 0
        for i in range(len(self.b)):
            sum += i
        print(sum)

    def avg(self):
        avg = 0
        for i in range(len(self.b)):
            avg += i
        avg = avg / 5
        print("%.1f" %avg)

cal1 = Calculator([1, 2, 3, 4, 5])
cal1.sum()
cal1.avg()
cal2 = Calculator([6, 7, 8, 9, 10])
cal2.sum()
cal2.avg()

# 4.	사용자로부터 리스트 형식 [data1],[data2],[data3]과 같은 형식으로 데이터를 입력받아, 한줄에 하나씩 데이터를 출력해라.
# ex) 입력: [aa],[bb],[cc],[dd]
#     출력: aa, bb, cc, dd

input_list = list(input("리스트 형식 입력").split(','))
text_str = ""
print(input_list)
for i in input_list:
    print(i.lstrip('[').rstrip(']'), end=" ")
print()

class Area:
    def __init__(self):
        self.i = 0
        self.j = 0
        self.color = ""

    def set(self, i, j, color):
        self.i = i
        self.j = j
        self.color = color

    def get(self):
        return self.i * self.j

a1=Area()
a2=Area()
a1.set(10,6,'red')
a2.set(4,4,'blue')
print(a1.get())
print(a2.get())

###########################################
# JSON 모듈 사용해서 파일 저장 후 읽기
import json
d = {"a":40,
     "b":("a", 5, 6),
     "c":"python"}

f = "test.json"
with open(f, "w") as f:
    json.dump(d, f) # 저장

with open("test.json", "r") as f:
    data = json.load(f)
    print(data)
    print(data["a"])
    print(data["b"])
    print(data["c"])
