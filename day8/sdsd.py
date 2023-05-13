import matplotlib.pyplot as plt
x=[]
y=[]
y12=[]
y2=[]
y22=[]
y3=[]
y32=[]
y4=[]
y42=[]
y5=[]
y52=[]
fruits=["apple","orange","cherry"]
score=[7,10,8]
cities=["seoul","newyork","london"]
scored=[70,80,60]
bar_color=["black"]
bar_color2=["yellow","orange","blue"]

subjects=["korean","math","science"]
score=[60,90,70]
for i in range(-10,11):
     x.append(i)
     y.append(i)
     y12.append(-i)
     y2.append(i**2)
     y22.append(-i**2)
     y3.append(i**3)
     y32.append(-i**3)
     y4.append(i+5)
     y42.append(i-5)
     y5.append(-i+5)
     y52.append(-i-5)
     fruits=["cherry","orange","apple"]
     numb=[40,80,50]
     alp=["L","N","S"]
     namb=[30,40,70]



figure,axes=plt.subplots(3,3)
axes[0,0].plot(x,y,'ro',x,y12,'bo')
axes[0,1].plot(x,y2,'go',x,y22,'ko')
axes[0,2].plot(x,y3,'bo',x,y32,'ro')
axes[1,0].bar(fruits,score,color=bar_color)
axes[1,1].bar(cities,scored,color=bar_color2)
axes[1,2].plot(x,y4,x,y42,x,y5,x,y52)
axes[2,0].barh(fruits,numb)
axes[2,1].barh(alp,namb)


plt.show()