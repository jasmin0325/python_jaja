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
<특6>
index
값으로 자리를 찾는 메소드
a=[100,200,300,400]
print(a.index(300))
답=2 300의 순서
중복된 값이 있을때는 맨 왼쪽거만 출력
리스트에 없는 값은 에러남
<특7>
indexing(문법)
자리로 값을 뽑아낸다
대괄호([])와 숫자 사용
b=[100,200,300,400]
print(b[1])
=200
left to rigth 방식에서는 0부터 시작
right to left방식에서는 -1부터 시작
<특8>
원하는 자리에 값을 추가할때 
insert 메소드 사용
c=["cherry',"apple","banana"]
c.insert(1,"orange")
print(c)
<특9>
원하는 값을 제거할때 remove 메소드 사용
c=["CHERRY","APPLE","BANANA"]
c.remove("CHERRY")
print(c)
<특10>
값들의 갯수를 셀때 count메소드 사용
d=[1,2,3,1,4]
print(d.count(1))
<특11>
리스트와 리스트를 결합할때
extend 메소드 사용
e=[1,2,3]
f=[4,5]
e.extend(f)
print(e)
<특12>
리스트와 리스트를 결합할때 
+ 연산자사용가능
g=[1,2,3,4]
h=[4,5]
print(g+h)
print(h+g)
<특 13>
함수,굳이 리스트와 같이 사용하지 않아도 됨
리스트의 길이를 알고싶을때 len함수 사용
i=[10,20,30]
print[len(i)]
=3
<특14>
fruits=["CHERRY","ORANGE","BANANA"]




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
# #1번문제 내림차순 정렬하기
# fruits=["blueberry","cherry","apple","watermelon"]
# fruits.sort()
# fruits.reverse()
# print(fruits)
# #1~20중 3의 배수를 리스트에 담아 내림차순정렬
# 배수=[]
# for i in range(1,21):
#     if i%3==0:
#         배수.append(i)
#         배수.sort()
#         배수.reverse()
# print(배수)
# #구구단(3)
# def 구구단(구구):
#     구구구=[]
#     for i in range(1,10):
#         구구구.append(i*구구)
#         구구구.sort()
#         구구구.reverse()
#     print(구구구)
# 구구단(3)
# a=[100,200,300,400,100]
# print(a.index(100))
# b=[100,200,300,400]
# print(b[0]+b[2])
# print(b[-1]-b[1])
# print(b[-2]%b[1])

# c=["cherry","apple","banana"]
# c.insert(1,"orange")
# c.insert(3,"수박")
# print(c)

# d=[1,2,3,1,4]
# print(d.count(5))

# fruits=["CHERRY","ORANGE","BANANA"]
# print(fruits[0])
# print(fruits[1])
# print(fruits[2])
fruits=["CHERRY","ORANGE","BANANA"]
fruits.append("WATERMELON")
fruits.insert(2,"BANANA")
fruits.sort()
fruits.reverse()

for i in range(len(fruits)):
    print(fruits[i])
삼배수=[]
for i in range(1,20):
    if i%3==0:
        삼배수.append(i)
print(삼배수)
for i in range(len(삼배수)):
    print(삼배수[i])