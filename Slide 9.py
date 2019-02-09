# Задиние 1

N=int(input('Введите число'))
a={0:1,1:1}
print(a)
for i in range(2,N,1):
    a[i]=a[i-2]+a[i-1]
print(a.values())
print(str(N) + '-й член последовательности = ' + str(max(a.values())))

#Задание 2

N=int(input('Введите число'))
a={0:1,1:1,2:1}
print(a)
for i in range(3,N,1):
    a[i]=a[i-3]+a[i-2]+a[i-1]
print(a.values())
print(str(N) + '-й член последовательности = ' + str(max(a.values())))

#Задание 3
N=int(input('Введите число'))
kvadr = {i : i**2 for i in range (1,N) if i%2!=0}
print(kvadr)

# Задание 4
a=int(input('Введите длину'))
b=int(input('Введите высоту'))
for i in range (b+1):
    if i==0 or i==b:
        print ('*' *a)
    else: print ('*'+ (a-2)*' ' + '*')



# Задание 5
summ=0
proiz=1
a=int(input('Введите 1-ое число'))
b=int(input('Введите 2-ое число'))
for i in range (a,b+1):
    summ+=i
    proiz*=i

print (summ, proiz)


# Задание 6
chet=[]
nechet=[]
a=int(input('Введите 1-ое число'))
b=int(input('Введите 2-ое число'))
chet =[i for i in range(a,b+1) if i%2==0]
nechet =[i for i in range(a,b+1) if i%2!=0]
print(chet)
print(nechet)

# Задание 7

_list=[1,-4,-5,6,-5,-2,2,6,7,-4,-5,-7]
pol=[]
otriz=[]
'''
for i in _list:
    if i>=0:
        pol.append(i)
    else: otriz.append(i)
print(pol)
print(otriz)
'''
pol= [i for i in _list if i>=0]
otriz= [i for i in _list if i<0]
print(pol)
print(otriz)