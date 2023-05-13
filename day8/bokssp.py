import matplotlib.pyplot as plt
plt.figure()
x=[]
y=[]
y2=[]
for i in range(-10,11):
    x.append(i)
    y.append(-i**2)
    y2.append(i**2)
plt.plot(x,y,x,y2)
plt.show()
print(x)
print(y)