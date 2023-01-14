'''
조건문
1번:if,else
if 조건:
    참일때 작성
else 조건:
    거짓일때 작설
2번:for
for 변수 in range(시작숫자,끝숫자)
    print(값)
for 변수 in range(시작,끝,증감):
    작성  
    '''
'''
apple=30
grape=10
if apple<grape:
    print("포도가 큼")
else:
    print("사과가 큼")

for i in range(3):
    print("hi")
    '''
 
# for i in range(1,11):
#     print(i)

# for i in range(2,11,2):
#     print(i)
'''for i in range(1,11):
    if i%2==1:
        print(i)'''
'''for i in range(2,11):
    if i%2==0:
        print(i)'''
'''합=0
for i in range(20,41):
    if i%3!=0:
        합+=i
print(합)'''
'''for i in range(50,101):
    if i%3==0:
      if i%4==0:
        print(i)'''
'''합=0
홀합=0
for i in range(1,101):
    if i%2==0:
        합+=i
    if i%2==1:
        홀합+=i
print(합-홀합)    
'''
곱=1
for i in range(10,31):
    if i%9==0:
        곱*=i
print(곱)

    
