#Задание 1
i=0
x=0
cap=1000
while x<cap:
    x= x+ 2**i
    i+=1
    print(x)
print(i)

# Задание 2 Решето Эратосфена

km=0
days=0
i=2
cap = 1000
a=list(range(100))
a[1] = 0
i = 2
while km <= cap:
    if a[i] != 0:
        km+=a[i]
        days+=1
        for j in range(i, 100, i):
            a[j] = 0
    i += 1

print (days,km)

# Задание 3
km=10
summ=10
i=1
while i<30:

    if i%2!=0:
        km=km+km*0.15
        i+=1
        print(i,km)

    else:
        i+=1
        print(i,km)
    summ += km
print(summ)

#Задание 4
km=10
summ=10
i=1
procent=0.1
while summ<100 and km<20:
    km=km+km*procent
    summ=summ+km
    i+=1
    print(i,km,summ)