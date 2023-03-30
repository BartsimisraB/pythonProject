'''
딕셔너리
'''
a = {'name': 'aa'}  # 딕셔너리 a 생성
a['sub'] = 'python'  # a에 key갑이 sub, value인 python 추가
print(a)

print(a['name'])  # 'name'의 value값 출력  aa
print(a.keys())  # key값 출력 - dict_keys(['name', 'sub'])
print(a.values())  # value값 출력 - dict_values(['aa', 'python'])
print(a.items())  # 각각의 key, value 쌍 출력 - dict_items([('name', 'aa'), ('sub', 'python')])
print('name' in a)  # a에 name 이라는 key가 존재하는지 여부 확인

'''
if 문
'''

'''x = 5
if x == 5:
    print(x)

a, b = map(int, input('두 정수 입력').split())

if a > b:
    print('>')
elif a < b:
    print('<')
elif a == b:
    print('==')

a = int(input('수 입력'))
sum = 0
for i in range(1,a,2):
    print(i)

for i in range(1,a):
    sum = sum + i
else:
    sum = sum + a
print(sum)

for i in range(1, a + 1):
    if(a % i == 0):
        print(i)
    else:
        pass'''

'''while True:
    inputA, inputB = map(int, input("두 정수 입력 : ").split())
    if inputA == 0 and inputB == 0:
        break
    else:
        print(inputA + inputB)
'''

# int() 정수형으로 변환하는 함수
# str() 문자열로 변환하는 함수
# float() 소수로 변환하는 함수

# 연결 연산자 + 를 이용해 문자열에 정수형을 넣는 경우
# 자바와 다르게 문자열로 변경을 해줘야 한다.
age = 23
message = "Happy" + str(age) + "Birthday"

'''# 딕셔너리 예시
dic = {"name": "TOM", "age": "11"}
print(dic["name"])

dic["pro"] = "hani"
print(dic)

del dic["name"]
print(dic)

s = set([1, 2, 3])
print(s)

s2 = list('abcdef')
print(s2)
print(s2[0:3])

# 집합 ( 중복 불가능 , 순서가 없다 )
s3 = set([4, 5, 6])
l3 = list(s3)
print(l3)
# print(s3[0]) 집합은 인덱싱으로 값을 얻을 수 없다.

s4 = set([1, 2, 3, 4, 5])
s5 = set([6, 7, 3, 4, 10])

print(s4 & s5)  # 교집합
print(s4.intersection(s5))  # 교집합

print(s4 | s5)  # 합집합
print(s4.union(s5))  # 합집합

print(s4 - s5)  # 차집합
print(s4.difference(s5))  # 차집합
'''

'''empty = {}  # 빈 딕셔너리
emptyList = list()  # 비어있는 리스트
emptyArr = []

active = True

while active:
    name = input("너의 이름은 ?")
    res = input("너는 한희를 좋아하니?")
    empty[name] = res

    ans = input("다른 사람한테 넘겨줄거니?")
    if ans == '아니' or '절대안돼':
        active = False

for i,j in empty.items():
    print(i + " " + j)'''

'''msg = 'hani 는 SEXY행'

for i in range(len(msg)):
    print(msg[i])
print()

for x in msg:
    if x.isupper():  # 대문자만 출력하겠다.
        print(x, end='')

print()

for x in msg:
    if x.islower():  # 소문자만 출력하겠다.
        print(x, end='')

print()

for x in msg:
    if x.isalpha():  # 알파벳인지 여부 확인.
        print(x, end='')

print()

tmp = "AZ"
for x in tmp:
    print(ord(x))  # ord : 아스키로 변환하는 함수

tmp = 65
print(chr(tmp))  # chr : 아스키를 변환하는 함수

a = []
for i in range(3, 31):
    if i % 3 == 0:
        a.append(i)
print(a)

q = [i for i in range(3, 31) if i % 3 == 0]
print(q)'''

'''a = [23, 12, 36, 53, 19]
print(a[0:3])

for x in enumerate(a):
    print(x)
    print(x[0], x[1])
print()
for x, y in enumerate(a):
    print(x, y)
print()

b = (1, 2, 3, 4, 5)

for index, value in enumerate(b):
    print(index, value)

# all : 모두 참이어야 한다.
if all(50 > x for x in a):
    print("Y")
else:
    print("N")

# any : 하나라도 참이어야 한다.
if any(15 > x for x in a):
    print("Y2")
else:
    print("N2")'''

# 이차원 반복문

a = [[0] * 3 for _ in range(3)]
print(a)  # [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
a[0][1] = 1
print(a)  # [[0, 1, 0], [0, 0, 0], [0, 0, 0]]

for x in a:
    for y in x:
        print(y)
    print()

