'''
리스트(list)
열거형 변수를 나타내는 자료구조중 하나
<문법>
c=[] #비어있는 리스트
d=[1,2,3,4] #숫자들을 리스트로 나타냄
e=["사과","바나나","귤"]#글을 리스트로 나타냄
f=[100,"cherry",200,"blueberry"]#숫자와 글을 혼용하여 나타냄
메소드
함수
<특1>
추가할때append메소드 사용,하나만 추가 가능
*맨 오른쪽애만 추가됨
<특2>
제거시 pop메소드 사용
*맨 오른쪽에만 제거됨
<특3>
전체삭제시 clear 메소드 사용
*사용시 빈 리스트로 정리됨
예)h=[1,"apple",2"blueberry"]
h.clear()
print(h)
<특4>
[2,4,1,3]
정렬:오름차순 정렬:작은수부터 큰수로[1,2,3,4],내림차순 정렬:큰수부터 작은수로[4,3,2,1]
오름차순:sort메소드사용
ex)i=[2,4,1,3]
i.sort()
print(i)
<특5>
역순 정렬할때reverse메소드 사용
[2,4,1,3]
--[3,1,4,2]




# f=[100,"cherry",200,"blueberry"]
# e=["apple","banana","lemon"]
# c=[]
# d=[1,2,3,4]
# print(c)
# print(d)
# print(e)
# print(f)
# g=[]
# g.append(1)
# print(g)
# g.append("apple")
# print(g)
# g.append(2)
# print(g)
# g.pop()
# print(g)
# g.pop()
# print(g)
i=[2,4,1,3]
i.sort()
print(i)
j=["blueberry","orange","apple"]
j.sort()
print(j)
k=[2,4,1,3]
k.reverse()
print(k)
'''
#1번문제 내림차순 정렬하기
fruits=["blueberry","cherry","apple","watermelon"]
fruits.sort()
fruits.reverse()
print(fruits)
#1~20중 3의 배수를 리스트에 담아 내림차순정렬
배수=[]
for i in range(1,21):
    if i%3==0:
        배수.append(i)
        배수.sort()
        배수.reverse()
print(배수)
#구구단(3)
def 구구단(구구):
    구구구=[]
    for i in range(1,10):
        구구구.append(i*구구)
        구구구.sort()
        구구구.reverse()
    print(구구구)
구구단(3)

