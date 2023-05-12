# 리스트
a=[]
a=['apple',10,False]
a[1]='test'
print(a[1])

#list slicing
a=[1,10,11,20,21,30,31]
x=a[1:4]
print(x)
y=a[::-1]
print(y)
b=["banana","drum",True,10,"apple"]
b.append(99.9)
b[1]=44
print(b)
del b[1]
print(b)
del b[1:3]
print(b)
b.remove(99.9)
print(b)
b.insert(0,'zero')
print(b)

x=[1,2,3,4]
y=['apple','banana']
z=x+y
print(z)

x.extend(y)
print(x)

z = x*3
print(z)

#중첩 리스트
q=['a','b','c']
w=[10,11,q,True,'string']

print(w[2][1:3])


# List comprehension 리스트 내포
num = list(range(1,11))
print(num)
lst=[i**2 for i in num]
print(lst)

lst2 = ['even' if i%2==0 else 'odd' for i in num]
lst3 = ['even' if i%2==0 else 'odd' for i in range(1,12)]
print(lst2)
print(lst3)
lst4 = [i**2 for i in range(10) if i%2==0]
print(lst4)