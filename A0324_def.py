'''
def add(a, b):
    c = a + b
    print(c)


add(3, 2)
add(5, 7)


def add(a, b):
    c = a + b
    return c


x = add(3, 2)
print(x)


def add(a, b):
    c = a + b
    d = a - b
    return c, d


print(add(3, 2))


def isPrime(x):
    for i in range(2, x):  # 2부터 x까지의 수 중 소수를 찾는 함수
        if x % i == 0:
            return False
    return True


a = [12, 13, 6, 7, 9, 19]
for y in a:
    if isPrime(y):
        print(y, end=" ")


def calcu(who, hour, num, price):
    msg = "할인 없음"
    if (hour == 15) and (num >= 3):
        price *= 0.9
        msg = "10% 할인"
    elif (hour == 12) and (num >= 5):
        price *= 0.8
        msg = "20% 할인"
    price = int(price)
    print("{0}씨는 {1} = {2}원".format(who, msg, price))


calcu("형민", 15, 4, 20000)
calcu("종진", 12, 5, 50000)
calcu("한빈", 10, 2, 70000)

x, y = map(int, input("x, y ?").split())


def mul(x, y):
    return x * y


print(mul(x, y))


def qq(a, b):
    for i in range(a, b + 1):
        print(i)

qq(1, 10)
qq(4, 6)
'''


def say(name, old=20, jender=True):
    print(name, old, sep="\n")
    if jender:
        print("남자")
    else:
        print("여자")
    print("---")


# 둘 다 남자로 나오는 이유
# 함수에서 지정된 매개변수의 순서를 맞춰주지 않으면
# default를 지정해도 함수에서 인식하지 못한다.
say('juli', True)
say('juli', False)


def say(name, old, jender):
    print(name, old, sep="\n")
    if jender:
        print("남자")
    else:
        print("여자")
    print('---')


say('juli', 25, False)

# 전역변수와 지역변수
a = 1


def vartest(a):
    a = a + 1  # 여기서 a는 함수 안에서만 이용하는 지역변수


print(vartest(a))  # None
print(a)  # 1


# 함수 밖의 변수 사용하기 - 잘 사용하지 않는다

def vartest(a):
    a = a + 1
    return a


print(vartest(a))  # 2


def vartest():
    global a
    a = a + 1


vartest()
print(a)  # 2


# lambda
def plus(x):
    return x + 10


print(plus(1))  # 11

plus = lambda x: x + 10  # lambda로 사용된 변수 명이 곧 함수명
print(plus(1))  # 11


# list와 map 이용해보기
def pp(x):
    return x + 20


print(list(map(pp, [3, 4, 5])))

# map(function, iterable) : 함수와 반복가능한 자료형을 입력으로 받는다.
# 1. 입력받은 자료형의 각 요소를 함수 f가 수행한 결과를 묶어서 돌려주는 함수
#
# 2. map함수의 반환값은 map 객체이므로 해당 자료형을
#    list 또는 tuple 형으로 형변환 해줘야 한다.
#
# 3. 두번째 인자로 들어오는 반복 가능한 자료형 (list 나 tuple)을
#    첫 번째 인자로 들어온 함수에 하나씩 집어넣어 함수를 실행한다.


# 1 ~ 5까지 list로 표현하는 방법
a = [i for i in range(1, 6)]
a2 = list(range(1, 6))
a3 = [1, 2, 3, 4, 5]

a4 = []
for i in a2:
    a4.append(i)
print(a4)


def one(i):
    return i


a5 = list(map(one, a2))
print(a5)

# one 함수를 람다식으로

one2 = list(map(lambda i: i, a2))
print(one2)

# divmod = 몫과 나머지를 튜플형식으로 반환
print(divmod(10, 3))  # (3,1)

for i, j in enumerate(['a', 'b', 'c']):
    print(i, j)

# eval - 문자열로 구성된 표현식을 입력으로 받아
#        해당 문자열을 실행한 결괏값을 리턴하는 함수
print(eval('1 + 2'))  # 3
print(eval('2 * 3 / 2'))  # 3.0


def po(n):
    re = []
    for i in n:
        if i < 0:  # 음수만 리스트에 저장
            re.append(i)
    return re


print(po([3, 4, 2, -2, 10, -3]))


#####################################
def pr(n):
    return n < 0


print(list(filter(pr, [3, 4, 2, -2, 10, -3])))
print(list(filter(lambda x: x < 0, [3, 4, 2, -2, 10, -3])))

################ 03 24 복습 ################
print(max([1, 5, 3]))
print(min([1, 3, 5]))
print(max("apple"))  # 나중에 나오는 문자가 큰 값
print(min("apple"))  # 나중에 나오는 문자가 작은 값

print(pow(2, 3))  # 2^3 = 8
print(2 ** 3)  # 2^3 = 8

print(round(4.8))  # 반올림
print(round(4.5893, 2))  # 소수점 3번째에서 반올림

print(sorted([3, 8, 4]))  # 리스트 오름차순 정렬

print(str('hello'.upper()))
print(str(10))  # 정수 10을 문자열로 형변환해서 출력

print(sum([1, 2, 3, 4, 5]))
print(sum(list(range(1, 6))))
print(sum(tuple(range(1,6))))

print(type("123"))  # <class 'str'>
print(type([1,2,3]))    # <class 'list'>
print(type(5))  # <class 'int'>
print(type(2.4))    # <class 'float'>
print(type((2,4)))  # <class 'tuple'>
print(type({1,2}))  # <class 'set'>
