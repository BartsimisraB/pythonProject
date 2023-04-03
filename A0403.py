# # 144p
# dic = {39: "Justin", 14: "John", 67: "Mike", 105: "Summer"}
# input_num = int(input("찾는 학생 번호 입력 : "))
# if input_num in dic:
#     print(dic[input_num])
# else:
#     print("?")
#
# # stack 문제
#
# 문제 7
# 스페이스로 띄어쓰기 된 단어들의 리스트가 주어질때,
# 단어들을 반대 순서로 뒤집어라.
# 각 라인은 w개의 영단어로 이루어져 있으며,
# 총 L개의 알파벳을 가진다.
#
# 각 행은 알파벳
# 과 스페이스로만 이루어져 있다.
# 단어 사이에는 하나의 스페이스만 들어간다.
# ex)
# 3
# this is a test Case   #1: test a is this
# foobar Case           #2: foobar
# all your base Case    #3: base your all
#
# input_str = list(map(str, input("단어를 공백으로 구분지어 입력 : ").split()))
# input_str = input_str[::-1]
# print(" ".join(input_str))
#
# #
#
# # 한희는 영어로 시는 쓰는 것을 좋아합니다.
# # 한희는 시를 쓰기 전에 시에 쓰일 단어를 미리 노트에 적어둡니다.
# # 이번에는 N개의 단어를 노트에 적었는데 시에 쓰지 않은 단어가 하나 있다고 합니다.찾아 주세요.
# #  입력설명
# # 첫 번째 줄에 자연수 N(3<=N<=100)이 주어진다.
# # 두 번째 줄부터 노트에 미리 적어놓은 N개의 단어가 주어지고, 이어 바로 다음 줄부터 시에
# # 쓰인 N-1개의 단어가 주어진다.
# # 출력설명
# # 첫 번째 줄에 시에 쓰지 않은 한 개의 단어를 출력한다.
# # 입력
# # 5
# # big
# # good
# # sky
# # blue
# # mouse
# # sky
# # good
# # mouse
# # big
# # 출력
# # blue
# def print_find_word():
#     never_used_word = ""
#     input_list = []
#     used_list = []
#     input_limit = int(input("몇개의 단어를 입력할 것인가요? : "))
#     for i in range(input_limit):
#         input_words = input("시에 사용할 단어 입력 : ")
#         input_list.append(input_words)
#     print("시에 사용할 단어 : " + " ".join(input_list))
#
#     for i in range(input_limit - 1):
#         input_used_words = input("시에 사용한 단어 입력 : ")
#         used_list.append(input_used_words)
#     print("시에 사용한 단어 : " + " ".join(used_list))
#
#     for j in input_list:
#         if j not in used_list:
#             never_used_word = j
#     print("시에 사용하지 않은 단어 : " + never_used_word)
#
# print_find_word()
# #
# # 딕셔너리로 만드는 방법
# n = int(input("몇개의 단어를 입력할 것인가요? : "))
# d = dict()
# for i in range(n):
#     m = input("시에 사용할 단어 입력 : ")
#     d[m] = 1    # {'big':1, 'blue':1,...}
#
# for i in range(n-1):
#     m = input("시에 사용할 단어 입력 : ")
#     d[m] =0    # {'sky':0, 'blue':0,...}
#
# for key, value in d.items():
#     if value == 1:
#         print(key)
#         break
#
# #
# 한 개의 회의실이 있는데 이를 사용하고자 하는 n개의 회의들에 대하여 회의실 사용표를 만들
# 려고 한다. 각 회의에 대해 시작시간과 끝나는 시간이 주어져 있고, 각 회의가 겹치지 않게 하
# 면서 회의실을 사용할 수 있는 최대수의 회의를 찾아라. 단, 회의는 한번 시작하면 중간에 중
# 단될 수 없으며 한 회의가 끝나는 것과 동시에 다음 회의가 시작될 수 있다.
# 입력
# 첫째 줄에 회의의 수 n(1<=n<=100,000)이 주어진다. 둘째 줄부터 n+1 줄까지 각 회의의 정
# 보가 주어지는데 이것은 공백을 사이에 두고 회의의 시작시간과 끝나는 시간이 주어진다.
# 출력
# 첫째 줄에 최대 사용할 수 있는 회의 수를 출력하여라.
# 입력예제
# 5
# 1 4
# 2 3
# 3 5
# 4 6
# 5 7
# 출력
# 3

n = int(input("총 회의의 수"))
meetings = []
for i in range(n):
    start, end = map(int, input().split())
    meetings.append((end, start))  # 끝나는 시간을 기준으로 오름차순 정렬하기 위해 end를 첫번째로 저장

# [(3, 2), (4, 1), (5, 3)]
meetings.sort()  # 끝나는 시간을 기준으로 오름차순 정렬

count = 0
end_time = 0
for meeting in meetings:
    if meeting[1] >= end_time:  # 회의를 진행할 수 있는 시간인 경우
        count += 1
        end_time = meeting[0]

print(count)
