# # 1 번
# A,B = input('두 과목의 점수 : ').split()
# sum = int(A) + int(B)
# print("두 과목의 평균 : %.1f" %(sum/2))
#
# # 2 번
# num_list = list()
# num_list = list(map(int, input("숫자 입력 : ").split()))
# num_list.sort()
# print(num_list[len(num_list)//2])

# 3 번
height_list = list()
nums = 0
for i in range(1, 9):
    A = input('키 입력 : ')
    A = int(A)
    height_list.append(A)
li_sum = sum(height_list)

for i in range(len(height_list)):
    if li_sum < 100:
        print(height_list)
    elif li_sum - height_list[i] == 100:
        break
    height_list.remove(height_list[i])
print(height_list)
