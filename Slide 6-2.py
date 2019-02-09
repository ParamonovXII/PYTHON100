name = "парамоноввладислав"

def function1s62(name):
    return ({i: i + 2 for i in range(((len(name) % 5) + 2) * 2)})

def function2s62(name):
    list_my = {i: i + 2 for i in range(((len(name) % 5) + 2) * 2)}
    list_my.update({i + len(list_my): list_my[i] + 1 for i in range(len(list_my))})
    return list_my

def function3s62(name):
    list_my = {i: i + 2 for i in range(((len(name) % 5) + 2) * 2)}
    list_my.update({i + len(list_my): list_my[i] + 1 for i in range(len(list_my))})
    return {i: list_my[i] for i in range(1, len(list_my) - 1)}

def function4s62(name):
    list_my = {i: i + 2 for i in range(((len(name) % 5) + 2) * 2)}
    list_my.update({i + len(list_my): list_my[i] + 1 for i in range(len(list_my))})
    return {i: list_my[i] for i in range(1, len(list_my), 3)}

def function5s62(name, n=1):
    list_my = {i: i + 2 for i in range(((len(name) % 5) + 2) * 2)}
    list_my.update({i + len(list_my): list_my[i] + 1 for i in range(len(list_my))})
    return {i: list_my[i] for i in range((n - 1) * round(len(list_my) / 3), round(n * len(list_my) / 3))}

if __name__ == "__main__":
    print(function1s62(name))
    print(function2s62(name))
    print(function3s62(name))
    print(function4s62(name))
    n = int(input("Введите часть списка которую хотите отобразить: "))
    print(function5s62(name, n))