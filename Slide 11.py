
def function1s11 (A,B,X,Y,Z,N=False):
    d=[]
    for i in range(A+1):
        for j in range(B+1):
            if i*X+j*Y==Z:
                N = True
                d.append("Номинал " + str(X) + " : " + str(i) + " Номинал " + str(Y) + " : " + str(j))

    if N==False: return False
    return d


def function2s11(word):
    if word==word[::-1]:
        return True


def function3s11 (A):
    A=abs(A)
    B=len(str(A))
    return B

def function4s11 (str1,str2,stroka):
    return stroka.replace(str1, str2)
