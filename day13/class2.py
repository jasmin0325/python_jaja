'''
클래스(class)
1. 생성자(constructor)
:객체를 생성할 때 자동으로 호출되는
method
init=initialization(초기화)
문법)class 클래스 이름:
       ->def __init__(self)
       ---->

'''
# class 수학:
#     원주율=3.141592
#     def 더하기(self,a,b):
#         결과=a+b
#         return 결과
# 초등수학=수학()
# print(초등수학.원주율)
# print(초등수학.더하기(2,3))

# class 수학:
#     def __init__(self,반지름):
#         self.원주율=3.141592
#         self.반지름=반지름
#     def 원넓이(self):
#         결과=self.원주율*self.반지름**2
#         return 결과
# # 중등수학=수학()
# # print(중등수학.원넓이(2))
# 고등수학=수학(2)
# print(고등수학.원넓이())
# class 댕댕이:
#     def __init__(self,이름,털색상):
#         self.이름=이름
#         self.털색상=털색상

#     def 소개하기(self):
#         print(f"강아지 이름은 {self.이름}이고 털은 {self.털색상}입니다")
# 삼촌네강아지=댕댕이("삼색이","3가지색")
# 친구집멍멍이=댕댕이("흰둥이","흰색")
# 우리집멍멍이=댕댕이("보리","노랑색")
# 우리집멍멍이.소개하기()
# 친구집멍멍이.소개하기()
# 삼촌네강아지.소개하기()
# class 은행:
#     def __init__(self,예금주,잔액):
#         self.예금주=예금주
#         self.잔액=잔액

#     def 입금(self,금액):
#         self.잔액=self.잔액+금액
#         print(f"{self.예금주}님의 현재 잔액은 {self.잔액}입니다.")
#     def 출금(self,금액):
#         self.잔액=self.잔액-금액
#         print(f"{self.예금주}님의 현재 잔액은 {self.잔액}입니다")
# 국민은행=은행("양의지",100000)
# 신한은행=은행("손흥민",10000)
# 국민은행.입금(3000)
# 국민은행.출금(50000)
# 신한은행.입금(1000)
# 신한은행.출금(5000)
class 연산:
    def __init__(self,첫번째수,두번째수):
        self.첫번째수=첫번째수
        self.두번째수=두번째수
    def 더하기(self):
        결과=self.첫번째수+self.두번째수
        print(f"{self.첫번째수}더하기{self.두번째수}는 {결과}입니다")
    def 빼기(self):
        결과=self.첫번째수-self.두번째수
        print(f"{self.첫번째수}빼기{self.두번째수}는 {결과}입니다")
    def 곱하기(self):
        결과=self.첫번째수*self.두번째수
        print(f"{self.첫번째수}곱하기{self.두번째수}는{결과}입니다")
    def 나누기(self):
        결과=self.첫번째수/self.두번째수
        print(f"{self.첫번째수}나누기{self.두번째수}는 {결과}입니다")

첫번째수=input("첫번째수:")
두번째수=input("두번째수:")
사칙연산=연산(int(첫번째수),int(두번째수))
사칙연산.더하기()
사칙연산.빼기()
사칙연산.곱하기()
사칙연산.나누기()

