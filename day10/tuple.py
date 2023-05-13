'''
튜플 (tuple)
-python 의 자료구조중 하나
-여러 값들을 모아둔 형태로 list와 비슷함
-list와 같이 indexing,slicing이 가능함
-list와 달리 소괄호를 이용해 값들을 저장
-튜플과 리스트의 차이점
 -리스트의 값은 mutable(변경가능)함
-튜플의 값은 immutable(변경불가)함
f string(f문자열)
-변수와 문자를 같이 작성하는 방법
-작성 방법-
-f"작성"
-f"{변수}"
input(입력)<->output(출력)


'''
# a=[1,2,3]
# b=(1,2,3)
# print(type(a),type(b))
# print(a[2],b[2])
# a=[1,2,3]
# a[2]=100
# a[1]=10
# print(a)
# b=(1,2,3)
# b[2]=100
# print(b)
# age=15
# name="junyoung"
# strl=f"나는{age}살 먹고,이름은{name}임"
# print(strl)
# age=20
# name="tonggyu"
# strl=f"나는{age}살 먹고,이름은{name}임"
# print(strl)
# animal="고양이"
# fruit="사과"
# strl=f"내가 좋아하는 동물은{animal}이고,과일은{fruit}입니다"
# print(strl)
# for i in range(0,3):
#     str=input("여기에 입력해줴요")
#     print(f"당신이 입력한 내용은{str}입니다 휴먼")
# for i in range(0,5):
#     animal=input("what animal do you like")
#     fruit=input("what fruit do you like")
#     print(f"당신이 입력한 좋아하는 동물은 {animal}이고,당신이 좋아하는 과일은{fruit}입니다. ")
for i in range(0,5):
    num1=input("첫번째수는?:")
    num2=input("두번째수는?:")
    print(f"두수의 합은{int(num1)+int(num2)}이다")