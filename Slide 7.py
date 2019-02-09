
def function1s7(text="парамоноввладислав", numb=5):
    return text * numb + "!"

def function2s7(chislo=10):
    for i in range(0, chislo+1):
        print(((chislo-1)-i) * '=' + ((i+1) * ' '))

def function3s7(word):
    return {i: word.count(i, 0, len(word)) for i in word}

def function4s7(text1):
    d = {}
    for word in text1.split():
        key = "слов длинной " + str(len(word))
        if key in d:
            d[key] += 1
        else:
            d[key] = 1
    return d



if __name__ == '__main__':
    print(zadanie71(text="парамоноввладислав", numb=5))
    print(zadanie72(chislo=10))
    print(zadanie73(word="парамоноввладислав"))
    print(zadanie74(text1="vcxvg dae adwedas dsaf dsarwr dxczdwe dfd"))