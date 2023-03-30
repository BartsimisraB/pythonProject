########### 모듈 임포트 ##################
#
# import A230327_2        # improt 모듈이름
# print(A230327_2.add(2,3))
# print(A230327_2.sub(3,4))
#
# from A230327_2 import add, sub  # from 모듈이름 import 함수명 : 해당 모듈의 함수 import
#
# print(add(4, 5))
# print(sub(2, 3))

# def hi():
#     print("hi")
#
# print(__name__)
## 직접 실행된 모듈 : __name__이라는 이름을 가진다.

def add(x,y):
    return x+y

if __name__=="__main__":
    print(add(3,2))
