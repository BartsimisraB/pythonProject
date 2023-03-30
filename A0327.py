"""
171p 파일 읽고 쓰기

파일 객체 = open("새파일.txt", '파일 열기 모드')
                                r - 읽기 모드 : 파일을 읽기만 할 때 사용
                                w - 쓰기 모드 : 파일에 내용을 쓸 때 사용
                                a - 추가 모드 : 파일의 마지막에 새로운 내용을 추가할 때 사용

## readline 함수 - 파일의 첫 줄만 인식 가능
: while문을 통해서 파일을 읽는 작업을 반복

f = open("C:/doit/새파일.txt", 'r')
while True:
    line = f.readline()
    if not line: break
    print(line)
f.close()


## readlines 함수 - 파일의 모든 줄을 인식 가능
: 모든 줄을 저장 가능하기에 반복문이 필요 x

f = open("C:/doit/새파일.txt", 'r')
lines = f.readlines()
for line in lines:
    print(line)
f.close

## append

with문과 사용하기 - 176p

"""
from builtins import str

# # with 문 예시
#
# # hello.txt 파일 생성 하기
# with open("hello.txt", 'w') as f:
#     f.write("hi")
#
# # read로 파일 읽어오기 - hi와 같이 문자열 형태로 읽어온다.
# with open("hello.txt", 'r') as f:
#     s = f.read()
#     print(s)
#
# # h.txt 파일 생성 하기
# with open("h.txt", 'w') as f:
#     for i in range(10):
#         f.write("{0}".format(i))
#
# # readlines로 파일 읽어 오기 - ['0123456789']처럼 리스트 형식으로 출력된다,
# with open("h.txt", 'r') as f:
#     l = f.readlines()
#     print(l)
#
# with open("h.txt", 'r') as f:
#     l = f.read()
#     print(l)

"""
 교재 157번 함수
  - 여러 개의 입력값을 받는 함수 만들기
"""


# def avg(*args):
#     sum = 0
#     for i in args:
#         sum += i
#     print(sum / len(args))
#
#
# avg(1, 2)
# avg(1, 2, 3, 4, 5)
#
#
# # 재귀함수
#
# def fac(n):
#     if n == 1:
#         return 1
#     return n * fac(n - 1)
#
#
# print(fac(5))


# def 함수이름(*매개변수)
#     수행할 문장
#     ...
#
# 여러개의 수를 입력받기 위해서는 매개변수 앞에 *를 붙여주어야 한다.

# () 개의 수를 입력 받아, 그 중애서 가장 큰 수를 출력하는 프로그램을 작성하라.
# def largest(*args):
#     if len(args) == 0:
#         return 0
#     else:
#         return max(args)

# max 함수

# numbers = []
# for i in range(10):
#     num = int(input("숫자를 입력하세요: "))
#     numbers.append(num)
#
# max_num = max(numbers)
# print("입력된 숫자 중 가장 큰 수는", max_num, "입니다.")

# # 람다 표현, 람다 호출
# def plus(x):
#     return x + 10
#
#
# print(plus(1))  # 11
#
# plus = lambda x: x + 10
# print(plus(1))  # 11
#
# # 람다 표현식 자체로 바로 호출하기!
# plus = (lambda x: x + 10)(1)
# print(plus)  # 11
#
#
# def pp(x):
#     return x + 10
#
#
# print(list(map(pp, [1, 2, 3])))
#
# # lamda로 바꿔서 출력
# print(list(map(lambda x: x + 10, [1, 2, 3])))
#
# # lamda 식에서는 elif 사용 불가능
# a = list(range(1, 11))
# print(list(map(lambda x: str(x) if x % 2 == 0 else x, a)))
#
# c = [15, 18, 32, 13, 23]
# # 15보다 크고 20보다 작은 값만 걸러서 출력
# print(list(filter(lambda x: x > 15 and x < 20, c)))
#
# # 183p ~
# """
# class 클래스이름:
#     def __init__(self,*arg): <<< 클래스 자신에 대한 객체 ( 생성자 역할 )
#         self.resilt = 0
#     def add(self, num):
#         self.result += num
#         return self.result
# cal1 = 클래스이름()
# cal2 = 클래스이름()
#
# 200p __init__ 메서드
# : setdata와 이름만 다르고 모든게 동일하다.
# 단, 메서드 이름이 특수 메서드를 의미하는 __를 사용한 __init__이므로
# 생성자로 인식되어 객체가 생성되는 시점에 자동으로 호출된는 차이가 있다.
# """
#
#
# # 클래스
# class Stu:
#     def __init__(self, name, age, adr):
#         self.hello = 'hi'  # 초기화
#         self.name = name  # 생성자 역할 수행
#         self.age = age
#         self.adr = adr
#
#     def hi(self):
#         print("{0} 나는 {1}이다.".format(self.hello, self.name))
#
#
# a = Stu('건용', 20, '서울')
# a.hi()
# print(a.name)
# print(a.age)
# print(a.adr)


###############################################################

# class Person:
#     def __init__(self, *args):  # *이 붙은 args에는 여러 인수가 들어올 수 있다.
#         self.name = args[0]
#
#     def hi(self):
#         print("{0}".format(self.name))
#
#
# m = Person(*['현석', '한희', '종진'])  # *을 붙여 사용한다.
# m.hi()


###############################################################

# class Calcu:
#     def __init__(self, num1, num2):
#         self.num1 = num1
#         self.num2 = num2
#
#     def sum(self):
#         print("{0}".format(int(self.num1) + int(self.num2)))
#
#     def minus(self):
#         print("{0}".format(int(self.num1) - int(self.num2)))
#
#
# a = Calcu(3, 4)
# a.sum()  # 7
# a.minus()  # -1


###############################################################

# class B:
#     def __init__(self):
#         self.li = []
#
#     def bag(self, a):
#         self.li.append(a)
#
#
# a = B()
# a.bag('가방')
#
# b = B()
# b.bag('책')
#
# print(a.li)
# print(b.li)


############## 정적 메소드 #########################
# class A:
#     @staticmethod  # 정적 메소드 : 매개변수에 self를 지정하지 않음
#     def add(a, b):
#         print(a + b)
#
#     @staticmethod
#     def minus(a, b):
#         print(a - b)
#
#
# A.add(4, 5)  # 정적 메소드기 때문에 객체 생성없이 클래스로부터 함수에 바로 접근 가능


#################  비공개 속성  ####################################

# class Stu2:
#     def __init__(self, name, age, adr):
#         self.hello = 'hi'
#         self.name = name
#         self.age = age
#         self.__adr = adr
#         # 변수 앞에 __를 붙여 비공개 속성으로 만듬 ( private와 유사 )
#         # 클래스 안에서만 사용할 수 있는 비공개 속성 : __속성명
#
#     def pr(self, n):
#         self.__adr += n  # 비공개 속성을 클래스 안에 있는 메소드에서만 접근 가능
#         print(self.__adr)
#
#
# a = Stu2('하니', 20, 3000)
# print(a.name)
# a.pr(3000)


# a.__adr += 3000     # 객체의 속성에 접근하는 방식 __속성명 :: 지금의 경우는 비공개 속성이므로 에러 발생
#
# Traceback (most recent call last):
#   File "C:\Users\...", line 263, in <module>
#     a.__adr += 3000     # 객체의 속성에 접근하는 방식 __속성명
#     ^^^^^^^
# AttributeError: 'Stu' object has no attribute '__adr'

##################  비공개 메소드  #####################################

# class Person2:
#     def __hi(self):  # 비공개 메소드 - __함수명
#         print('hello')
#
#     def hello(self):
#         self.__hi()  # 클래스 안에서 비공개 메소드 호출 가능
#
#
# c = Person2()
# c.hello()
# c.__hi()  #   클래스 밖에서 비공개 메소드 호출 불가능
# Traceback (most recent call last):
#   File "C:\Users\11027\PycharmProjects\pythonProject\A0327.py", line 284, in <module>
#     c.__hi()
#     ^^^^^^
# AttributeError: 'Person2' object has no attribute '__hi'

#########################################################################

# import random
#
# fruit = ['apple', 'banana', 'mango']
# a = random.randint(0, len(fruit) - 1)
# print((fruit[a]))


#########################################################################

class Student:
    def __init__(self, id, name, score=0):
        self.id = id
        self.name = name
        self.score = score

    def getId(self):
        return self.id

    def getName(self):
        return self.name

    def setScore(self, score):
        self.score = score

    def getScore(self):
        return self.score


class Cal:
    def __init__(self):
        self.stu = []  # 리스트로 초기화

    def add(self, student):
        self.stu.append(student)  # 비어있는 리스트에 값 추가
        # [ID, name, score, 2, 건용, ...]

    def avg(self):
        sum = 0
        for i in self.stu:
            sum += i.getScore()
        average = sum / len(self.stu)
        return average


a = Student(1, '종진')
a.setScore(80)
a2 = Student(2, '건용', score=90)
a3 = Student(3, '형민', score=95)
a4 = Student(4, '한희', score=79)

c = Cal()
c.add(a)
c.add(a2)
c.add(a3)
c.add(a4)

print(f"평균 : {c.avg()}")

num = list(range(50, 71))
print(list(filter(lambda x: x % 2 == 0, num)))
print(list())

#####################################################################

class Person:
    def __init__(self):
        print('안녕하세요')

class Student(Person):
    def __init__(self):
        print('공부하세요')
        super().__init__()  # 부모 클래스(Person)의 __init__ 메소드 호출

a=Person()
# a.hi()
# a.study()

b=Student()
# b.hi()
# b.study()

####################################################################

class Super:
    def a(self):
        print("super")

class Sub:
    def b(self):
        print("sub")

class Sub2(Super,Sub): #다중 상속
    def c(self):
        print("sub2")
s=Sub2()
s.a()
s.b()
s.c()