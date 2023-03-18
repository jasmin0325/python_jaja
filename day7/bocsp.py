# import matplotlib.pyplot as plt
# plt.figure()
# x=[]
# y=[]
# for i in range(-10,11):
#     x.append(i)
#     y.append(-2*i+1)
# plt.plot(x,y)
# plt.show()
import matplotlib.pyplot as plt
x=[]
y=[]
x1=[]
y1=[]
x2=[]
y2=[]
x3=[]
y3=[]
for i in range(-10,11):
    x.append(i)
    y.append(-i)
    x1.append(i)
    y1.append(i*i)
    x2.append(i)
    y2.append(i)
    x3.append(i)
    y3.append(-(i*i))
plt.plot(x,y,'o',x1,y1,'o',x2,y2 ,'o',x3,y3,'o')
plt.show()
# plt.figure()
# plt.plot([-1,0],[0,1],[1,0],[0,-1],[-1,0],[0,-1],[1,0],[0,1])
# plt.xlabel("x")
# plt.ylabel("y")
# plt.show()


# plt.figure()
# x=[]
# y=[]
# for i in range(-20,21):
#     x.append(i)
#     y.append(-(i*i)+2*i+3)


# for i in range(-30,31):
#     x.append(i)
#     # y.append(2*(i*i*i)-8)

# x1=[]
# y1=[]
# x2=[]
# y2=[]
# for i in range(-10,11):
#     x1.append(i)
#     y1.append(2**i)
#     x2.append(i)
#     y2.append(1/2**i)