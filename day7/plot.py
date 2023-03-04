
# 모듈설치
#pip install 모듈이름
#모듈 가져오기
#import 모듈이름
#모듈사용하기
#모듈이름.변수
#모듈이름.함수()
# import matplotlib.pyplot as PLT
# PLT.figure()
# PLT.plot([50,40,60],[150,120,170],'o')
# PLT.ylabel("height")
# PLT.xlabel("weight")
# PLT.show()

# import matplotlib.pyplot as PLT
# xvalues=[]
# yvalues=[]

# for i in range(-100,101):
#     xvalues.append(i)
#     y=i*i
#     yvalues.append(y)
# print(xvalues)
# print(yvalues)
# PLT.figure()
# PLT.plot(xvalues,yvalues,'r')
# PLT.ylabel("y")
# PLT.xlabel("x")
# PLT.show()
# xvalues=[]
# yvalues=[]
# for i in range(6):
#     xvalues.append(i)
#     y=3*i+5
#     yvalues.append(y)
# print(xvalues)
#print(yvalues)
import matplotlib.pyplot as PLT
xvalues=[]
yvalues1=[]
yvalues2=[]
yvalues3=[]

for i in range(-10,11):
    xvalues.append(i)
    yvalues1.append(i)
    yvalues2.append(i*i)
    yvalues3.append(i**3)
print(xvalues)
print(yvalues1)
PLT.figure()
PLT.plot(xvalues,yvalues1,'r',xvalues,yvalues2,'g',xvalues,yvalues3,'b')
PLT.ylabel("y")
PLT.xlabel("x")
PLT.show()