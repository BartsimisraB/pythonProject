''' 정규 표현식 '''
import re

w = ['orange', 'order', 'october', 'march', 'young', 'bccaacy']

p = r"oc.*"  # oc.* : oc로 시작하는 모든 문자, * : 반복
for i in w:
    if re.match(p, i):  # p에 해당하는 조건과 일치하는지 여부
        print(i)

# b 로 시작하고 y 로 끝나는 패턴
ac = r"b.*y"
for i in w:
    if re.match(ac, i):
        print(i)

# search
# search(r"조건식", "비교할 문자")
print(re.search(r"^abc$", "abc"))  # <re.Match object; span=(0, 3), match='abc'>
# ^ : 모든 문자, $ : 문자열의 끝을 지정
print(re.search(r"^abc$", "abcd"))  # None
print(re.search(r"^abc$", "xbcd"))  # None

##############

w = ['soup', 'spot', 'book', 'notebook']
p = r"^s...$"  # s 로 시작하고 총 길이가 4인 글자
a = [i for i in w if re.search(p, i)]  # 내포 함수로 search 사용
print(a)

##############

print(re.search(r"ba*", "b"))
print(re.search(r"ba{1,3}", "baaaaaaa"))  #

s = "I like red colour"  # \w : 문자 + 숫자
p = r"\w+(color|colour)"  # 'color'와 'colour' 중 하나가 나타나는 패턴을 찾습니다.
print(re.search(p, s))
