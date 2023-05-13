'''dictionary:딕셔너리
-python에서 사용하는자료구조
-key와 value의 쌍으로 이루어짐
-중괄호와:을 이용해 작성
ex){"손흥민":"축구":"류현진":"야구"}
-indexing가능 ->key이용->get method 이용해도 됨
또는 update method를 이용해 value쌍을 추가할수 있음
-key in dictionary 질문에 true orfalse로 확인가능
'''
'''height={"용규":177,"자민":200,"재민":125,"준영":101}
print(type(height))
리스트=[177,200,125,101]
튜플=(177,200,125,101)
print(리스트[1])
print(튜플[1])
print(height["자민"])
print('jammin say,"what?"')
print(height.keys())
print(height['준영'])
print(height.get("준영"))
리스트[1]=150
print(리스트)
height["자민"]=150
print(height)
height.update({"자민":149.9})
print(height)
height["선생님"]=180
print(height)
height.update({"손흥민":185})
print(height)
del height["손흥민"]
del height["선생님"]
print(height)
print("용규"in height)
print("손흥민"in height)'''
fruits={"orange":50,"banana":30,"apple":40}
fruit=input("this is fruit store.what do you want?:")
if fruit in fruits:
    print(f"we have {fruit},{fruits[fruit]} left")
else:
    print(f"sorry,we don't have {fruit}")
