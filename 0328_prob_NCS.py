# # 322p
# # 1 번
# a = "a:b:c:d"
# b = "#".join(a.split(":"))
# print(b)
#
# # 2 번
# a = {'A': 90, 'B': 80}
# a['C'] = 70
# print(a['C'])
#
# # 3 번
# # 리스트 더하기는 두 리스트를 더해 새로운 리스트를 반환하는 방식이며,
# # extend는 기존의 리스트에 데이터를 추가하는 방식으로 두 방식에 차이가 있다.
#
# # # 4 번
# A = [20, 55, 67, 82, 45, 33, 90, 87, 100, 25]
# sum_num = 0
# for i in A:
#     if i < 50:
#         pass
#     else:
#         sum_num += i
# print(sum_num)
#
# # # 5 번
# def calp():
#     input_num = int(input("수 입력 : "))
#     num = 0
#     i = 1
#     start_num = 0
#     start_num2 = 1
#
#     while i <= input_num:
#         if i == 2 | i == 3:
#             print(start_num, end=" ")
#         else:
#             print(num, end=" ")
#         num = start_num + start_num2
#         start_num = start_num2
#         start_num2 = num
#         i += 1
#
# calp()
# print()
# # # 6 번
#
# input_num = list(map(int, input('숫자 입력 : ').split(',')))
# print(input_num)
# sum_num = sum(input_num)
# print(sum_num)
#
# # # 7 번
# num_two = int(input("구구단 출력할 숫자를 입력하세요 : "))
# for i in range(1,10):
#     print(num_two * i, end=" ")
# print()
#
# # 8 번
#
# with open('abc.txt','w') as f:
#     f.write('AAA\n')
#     f.write('BBB\n')
#     f.write('CCC\n')
#     f.write('DDD\n')
#     f.write('EEE')
#
# with open('abc.txt', 'r') as g:
#     lines = g.readlines()
# lines.reverse()
#
# g = open('abc.txt', 'w')
# for line in lines:
#     line = line.strip()     # 포함되어 있는 줄 바꿈 문자 제거
#     g.write(line)
#     g.write('\n')
# g.close()
#
# # 9 번
# with open('sample.txt', 'r') as f:
#     lines = f.readlines()
# f.close()
#
# total = 0
#
# for line in lines:
#     score = int(line)
#     total += score
# average = total / len(lines)
#
# with open('result.txt', 'w') as g:
#     g.write('총 점수 : ' + str(total) + '\n')
#     g.write('평균 점수 : ' + str(average))
# g.close()
#
# # 10 번
# class Calculator:
#     def __init__(self, a):
#         self.a = a
#         self.total = 0
#         self.average = 0
#     def sum(self):
#         self.total = sum(self.a)
#         print(self.total)
#     def avg(self):
#         self.average = self.total / len(self.a)
#         print(self.average)
#
# cal1 = Calculator([1,2,3,4,5])
# cal1.sum()
# cal1.avg()
#
# # 11 번
#
# # 12 번
# result = 0
# try:
#     [1,2,3][3]
#     "a" + 1
#     4 / 0
# except TypeError:
#     result += 1
# except ZeroDivisionError:
#     result += 2
# except IndexError:
#     result += 3
# finally:
#     result += 4
#
# print(result)
# # 7 출력 >> [1,2,3][3] 에서 IndexError가 출력된 후
# # finally로 넘어가기 때문에 3 + 4 로 7이 출력된다.
#
# # 13 번
#
# def DashInsert(nums):
#     result = []
#     for i in range(0, len(nums) - 1):
#         result.append(nums[i])
#         if nums[i] % 2 == 0 and nums[i + 1] % 2 == 0:
#             result.append('*')
#         elif nums[i] % 2 == 1 and nums[i + 1] % 2 == 1:
#             result.append('-')
#     result.append(nums[-1])
#     return result
#
# nums = list(map(int, input('숫자 입력 : ')))
# result_nums = list(map(str,DashInsert(nums)))
# print("".join(result_nums))
#
## 14 번
# def seq_str():
#     input_str = input("문자열 입력 : ")
#
#     if not input_str:    # 빈 문자열 예외처리
#         return ""
#
#     count = 1
#     result = []
#
#     for i in range(1, len(input_str)):
#         if input_str[i] == input_str[i - 1]:    # 문자열이 연속으로 나오는 경우
#             count += 1
#         else:                                   # 문자열이 반복되지 않은 경우
#             result.append(input_str[i - 1])
#             result.append(str(count))
#             count = 1
#
#     # 마지막 문자 처리
#     result.append(input_str[-1])
#     result.append(str(count))
#
#     return "".join(result)
#
#
# print(seq_str())
#
# # 15 번
# zero_to_ten = "0123456789"
# list_zero_to_ten = list(str(zero_to_ten))  # ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
#
#
# def duplicate_number():
#     input_check_num = list(map(str, input("입력 : ").split()))
#     result = []
#     # 0 - 9 를 한번씩 사용한 것인지 여부 판단
#     for i in range(0, len(input_check_num)):
#         check_num = list(map(str, input_check_num[i]))
#         sort_check_num = check_num.sort()
#         print(check_num)
#         if len(list_zero_to_ten) != len(check_num) and list_zero_to_ten != sort_check_num:
#             result.append('false')
#         elif len(list_zero_to_ten) == len(set(check_num)) and list_zero_to_ten.__eq__(sort_check_num):
#             result.append('true')
#     print(result)
#
# duplicate_number()
#
# # 19 번
#
# import re
#
# s = '''
# park 010-9999-9988
# kim 010-9909-7789
# lee 010-8789-7768
# '''
# p = re.compile(r"(\w+\s\d{3}-\d{4})-\d{4}")
# result = p.sub("\g<1>-####", s)
# print(result)
#
# # 20 번
#
# import re
# p = re.compile(".*[@].*[.]?(.com$|.net$).*$")
# print(p.match("park@naver.co.kr"))
# print(p.match("park@naver.com"))

##################################################
# # 179p
# # 1 번
# number % 2 == 1
#
# # 2 번
# *args , result / len(args)
#
# # 3 번
# 두 수를 입력한 경우 str 형으로 입력되기 때문에 3 + 6 = 36이 나온다.
# input1, input2 = map(int, input("첫번째 숫자 입력, 두번째 숫자 입력 : ").split())
# total = input1 + input2
# print(total)
#
# # 4 번
# print("you" "need" "python")
# print("you"+"need"+"python")
# print("you","need","python")    # , 로 인해 공백이 추가로 생성되어 출력된다.
# print("".join(["you","need","python"]))
#
# # 5 번
# with open("test.txt", "w") as f1:
#     f1.write("Life is too short")
#
# with open("test.txt", "r") as f2:
#     f3 = f2.read()
#     print(f3)
#
# 6 번
# a , \n
#
# 7 번
# f.read()
# body.replace('java','python')
# 'w'
#
###########################################
# # 262p -
# # 1 번
# class Calculator:
#     def __init__(self):
#         self.value = 0
#     def add(self, val):
#         self.value += val
#
# class UpgradeCalculator(Calculator):
#     def __init__(self):
#         self.value = 0
#
#     def minus(self, val):
#         self.value -= val
#
# cal = UpgradeCalculator()
# cal.add(10)
# cal.minus(7)
# print(cal.value)
#
# # 2 번
# class Calculator:
#     def __init__(self):
#         self.value = 0
#
#     def add(self, val):
#         self.value += val
#
#
# class MaxLimitCalculator(Calculator):
#     def add(self, val):
#         self.value += val
#         if self.value > 100:
#             self.value = 100
#
#
# cal = MaxLimitCalculator()
# cal.add(60)
# cal.add(50)
# print(cal.value)
#
# # 3 번
#
# 1. all 함수는 포함하고 있는 요소가 전부 참인 경우 True를 반환하고, 하나라도 거짓인 경우 False를 반환한다.
# 요소에 0이 포함되어 있으므로 False를 반환한다.
# 2. ord('a') 는 a 의 아스키번호 97을 반환하며, char(97)을 통해 다시 'a'가 출력된다.
#
# # 4 번
#
# a = [1, -2, 3, -5, 8, -3]
# b = list(filter(lambda x: x > 0, a))
# print(b)
#
# # 5 번
#
# print(int('0xea', 16))
#
# # 6 번
#
# b = [1,2,3,4]
# a = list(map(lambda x: x * 3, b))
# print(a)
#
# # 7 번
#
# a = [-8, 2, 7, 5, -3, 5, 0, 1]
# a.sort()
# print(a[0] + a[-1])
#
# # 8 번
#
# print(round(17/3, 4))
#