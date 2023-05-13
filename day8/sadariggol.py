import matplotlib.pyplot as plt
plt.figure()
x=[]
y1=[]
y2=[]
y3=[]
y4=[]

for i in range(-5,6):
    x.append(i)
    y1.append(5)
    y2.append(-5)
    y3.append(5*i+10)
    y4.append(-5*i+10)
plt.plot(x,y1,x,y2,x,y3,x,y4)
plt.show()
print(x)
print(y1,y2,y3,y4)