'''
    선택 정렬
    - 주어진 데이터 중 최솟값을 찾음
    - 해당 최솟값을 데이터 맨 앞에 위치한 값과 교환

    => 처리되지 않는 데이터 중에서 가장 작은 데이터를 선택해 맨 앞의 데이터와 바꾸는 것을 반복
    ex) data = [8, 3, 2, 1]
        1차 : 1, 3, 2, 8
        2차 : 1, 2, 3, 8 ... done

'''


# 91p 8-1번
def sort_num(a):
    n = len(a)
    for i in range(0, n - 1):
        min_idx = i
        for j in range(i + 1, len(a)):
            if a[min_idx] > a[j]:
                min_idx = j
        a[min_idx], a[i] = a[i], a[min_idx]


d = [2, 4, 5, 1, 3]
sort_num(d)
print(d)

'''
    삽입 정렬
    - 두번째 인덱스부터 시작
    - 해당 인덱스 (key)앞에 있는 데이터(A)부터 비교해 key값이 더 작으면 A값을 뒤 인덱스로 복사
    - key값이 더 큰 데이터를 만날 때까지 반복
    - 큰 데이터를 만난 위치 바로 뒤에 key값을 이동시킨다.
    ex) data = [8, 3, 2, 5]
    8
    3 8
    2 3 8 
    2 3 5 8
'''

'''
N명의 학생의 수학점수가 주어집니다. N명의 학생들의 평균(소수 첫째자리 반올림)을 구하고,
N명의 학생 중 평균에 가장 가까운 학생은 몇 번째 학생인지 출력하는 프로그램을 작성하세
요.
평균과 가장 가까운 점수가 여러 개일 경우 먼저 점수가 높은 학생의 번호를 답으로 하고, 높
은 점수를 가진 학생이 여러 명일 경우 그 중 학생번호가 빠른 학생의 번호를 답으로 합니다.

입력
첫줄에 자연수 N(5<=N<=100)이 주어지고, 두 번째 줄에는 각 학생의 수학점수인 N개의 자연
수가 주어집니다. 학생의 번호는 앞에서부터 1로 시작해서 N까지이다.
출력
첫줄에 평균과 평균에 가장 가까운 학생의 번호를 출력한다.
평균은 소수 첫째 자리에서 반올림합니다.

입력예제
10
45 73 66 87 92 67 75 79 75 80
출력
74 7
'''


def average_score():
    N = int(input("몇 명의 학생의 점수를 입력? : "))
    score = list(map(int, input(str(N) + " 명의 학생의 점수를 입력 : ").split()))
    score.sort()

    middle = set()
    total = sum(score)
    stu_idx = 0

    average = total / N
    average = int(round(average, 0))

    for i in range(len(score)):
        middle.add(abs(average - score[i]))
    middle_list = list(middle)

    for i in range(len(middle_list) - 1):
        for j in range(i + 1, len(middle_list)):
            if middle_list[i] < middle_list[j]:
                stu_idx = i + 1
            elif middle_list[i] == middle_list[j]:
                stu_idx = i + 1

    print(average, stu_idx)


average_score()
