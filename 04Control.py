# 제어문
# 조건문
# score = int(input('점수입력:'))
score = 100
grade = ''
if score<=100 and score>=85:
    grade='우수'
elif score>=70:
    grade='보통'
else:
    grade='부족'
print('당신의 점수: %d / 등급: %s'%(score,grade))

num=5
result = 0
if num>6:
    result = num*2
else:
    result = num+2
print(result)

print(num*2 if num>6 else num +2)

# 반복문
# while문
cnt = tot = 0
datalst=[]
while cnt<5:
    cnt+=1
    tot+=cnt
    datalst.append(cnt)
    print(cnt, tot)
print(datalst)

# 1 - 100까지의 4의 배수의 합
cnt = tot = 0
datalst=[]
while cnt <100:
    cnt+=1
    if cnt%4==0:
        tot+=cnt
        datalst.append(cnt)
print('1-100까지 4의 배수의 합:%d'%(tot))
print(datalst)

i=0
while i<10:
    i+=1
    if i==3:
        continue
    if i==6:
        break
    print(i,end=' ')
    

#for문
string='abcdefghijklmn'
print(len(string))
for s in string:
    print(s)

lst = [1,2,3,4,5,6,7]
for e in lst:
    print(e)
print()
print(range(10))
for e in range(10):
    print(e)
print()
for e in range(3,10):
    print(e)
print()
for e in range(1,10,2):
    print(e,end=' ')
print()

lst=['A','B','C']
if 'B' in lst:
    print("Ok")
else:
    print('No')
    
    
    
    



