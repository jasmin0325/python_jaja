배열=[-1,1,3,-2,2]
음수=[]
양수=[]
for i in 배열:
    if i<0:
        음수.append(i)
    else:
        양수.append(i)
print(음수+양수)


