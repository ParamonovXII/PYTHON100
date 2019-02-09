name = "парамоноввладислав"

def function1s61(name):
    return [i + 1 for i in range(((len(name) % 5) + 2) * 2)]

def function2s61(name):
    list_my = [i + 1 for i in range(((len(name) % 5) + 2) * 2)]
    return list_my + [i + 1 for i in list_my]

def function3s61(name):
    list_my = [i + 1 for i in range(((len(name) % 5) + 2) * 2)]
    list2 = list_my + [i + 1 for i in list_my]
    return list2[1:-1]

def function4s61(name):
    list_my = [i + 1 for i in range(((len(name) % 5) + 2) * 2)]
    list2 = list_my + [i + 1 for i in list_my]
    return [list2[i] for i in range(1, len(list2), 3)]

def function5s61(name, n=1):
    list_my = [i + 1 for i in range(((len(name) % 5) + 2) * 2)]
    list2 = list_my + [i + 1 for i in list_my]
    return [list2[i] for i in range((n - 1) * round(len(list2) / 3), round(n * len(list2) / 3))]


if __name__ == "__main__":
    print(function1s61(name))
    print(function2s61(name))
    print(function3s61(name))
    print(function4s61(name))
    n = int(input("Введите часть списка которую хотите отобразить(1,2 или 3): "))
    print(function5s61(name, n))


