import numpy as np

def string_compare(P: str, T: str, i: int, j: int):
    if P == T:
        return 0

    if i == 0:
        return j
    elif j == 0:
        return i

    zamian = string_compare(P, T, i - 1, j - 1) + (P[i] != T[j])
    wstawien = string_compare(P, T, i, j - 1) + 1
    usuniec = string_compare(P, T, i - 1, j) + 1

    min_cost = min(zamian, wstawien, usuniec)

    return min_cost


def PD_string_compare(P: str, T: str, i = None, j = None, D = None, parents = None):
    if P == T:
        return 0, [], []

    if i is None or j is None:
        i = len(P) - 1
        j = len(T) - 1

    if D is None:
        D = [[0] * (len(T)) for _ in range(len(P))]
        for k in range(len(P)):
            D[k][0] = k
        for k in range(len(T)):
            D[0][k] = k

    if parents is None:
        parents = [['X'] * (len(T)) for _ in range(len(P))]
        for k in range(len(P)):
            parents[k][0] = 'D'
        for k in range(len(T)):
            parents[0][k] = 'I'

    for k in range(1, len(P)):
        for m in range(1, len(T)):
            zamiany = D[k-1][m-1] + (P[k] != T[m])
            wstawienia = D[k][m-1] + 1
            usuniecia = D[k-1][m] + 1

            lista = [zamiany, wstawienia, usuniecia]
            mini = min(lista)
            D[k][m] = mini
            idx = lista.index(mini)
            type = ''
            if idx == 0:
                if T[m] == P[k]:
                    type = 'M'
                else:
                    type = 'S'
            elif idx == 1:
                type = 'I'
            else:
                type = 'D'

            parents[k][m] = type
        parents[0][0] = 'X'

    return D[len(P) - 1][len(T) - 1], D, parents

def znajdowanie_sciezki(parent):
    i = len(parent) - 1
    j = len(parent[0]) - 1
    result = ''
    temp = parent[i][j]
    while temp != 'X':
        result += temp
        if temp == 'D':
            i -= 1
        elif temp == 'I':
            j -= 1
        else:
            i -= 1
            j -= 1
        temp = parent[i][j]
    return result[::-1]

def dopasowanie(P, T):
    p_size = len(P)
    t_size = len(T)
    D = [[0 for j in range(t_size)] for i in range(p_size)]
    for i in range(p_size):
        D[i][0] = i
    parent = [['X' for j in range(t_size)] for i in range(p_size)]
    for i in range(p_size):
        parent[i][0] = 'D'
    for j in range(t_size):
        parent[0][j] = 'I'

    for i in range(1, p_size):
        for j in range(1, t_size):
            z = D[i - 1][j - 1] + (P[i] != T[j])
            w = D[i][j - 1] + 1
            u = D[i - 1][j] + 1
            temp = [z, w, u]
            mini = min(temp)
            D[i][j] = mini
            idx = temp.index(mini)
            type = ''
            if idx == 0:
                if T[j] == P[i]:
                    type = 'M'
                else:
                    type = 'S'
            elif idx == 1:
                type = 'I'
            else:
                type = 'D'

            parent[i][j] = type
    parent[0][0] = 'X'
    end = D[-1].index(min(D[-1]))
    start = end - p_size + 2
    return start, end

def sekwencja_(parent, p):
    i = len(parent) - 1
    j = len(parent[0]) - 1
    result = ''
    temp = parent[i][j]
    while temp != 'X':
        if temp == 'D':
            i -= 1
        elif temp == 'I':
            j -= 1
        elif temp == 'M':
            result += p[i]
            i -= 1
            j -= 1
        else:
            i -= 1
            j -= 1
        temp = parent[i][j]
    return result[::-1]

def sekwencja(P, T, D = None, parents = None):
    p_size = len(P)
    t_size = len(T)
    D = [[0 for j in range(t_size)] for i in range(p_size)]
    for i in range(p_size):
        D[i][0] = i
    for j in range(t_size):
        D[0][j] = j
    parent = [['X' for j in range(t_size)] for i in range(p_size)]
    for i in range(p_size):
        parent[i][0] = 'D'
    for j in range(t_size):
        parent[0][j] = 'I'

    for i in range(1, p_size):
        for j in range(1, t_size):
            x = 0
            if T[j] != P[i]:
                x = np.inf
            z = D[i - 1][j - 1] + x
            w = D[i][j - 1] + 1
            u = D[i - 1][j] + 1
            temp = [z, w, u]
            mini = min(temp)
            D[i][j] = mini
            idx = temp.index(mini)
            type = ''
            if idx == 0:
                if T[j] == P[i]:
                    type = 'M'
                else:
                    type = 'S'
            elif idx == 1:
                type = 'I'
            else:
                type = 'D'

            parent[i][j] = type
    parent[0][0] = 'X'
    result = sekwencja_(parent, P)

    return result

def sort_t(t):
    p = ' '
    temp = t
    temp = temp.replace(' ', '')
    t_list = []
    for el in temp:
        t_list.append(int(el))
    t_list.sort()
    for el in t_list:
        p += str(el)
    return p

def print_matrix(M):
    for i in range(len(M)):
        print(M[i])

P = ' kot'
T = ' pies'
result = string_compare(P, T, len(P) - 1, len(T) - 1)
print(result)

P = ' biały autobus'
T = ' czarny autokar'
result, _, __ = PD_string_compare(P, T, len(P) - 1, len(T) - 1)
print(result)


P = ' thou shalt not'
T = ' you should not'
result, D, parents = PD_string_compare(P, T, len(P) - 1, len(T) - 1)

print(znajdowanie_sciezki(parents))

P = ' ban'
T = ' mokeyssbanana'
start, end = dopasowanie(P, T)
print(start)


P = ' democrat'
T = ' republican'
sekwens = sekwencja(P, T)
print(sekwens)

T = ' 243517698'
P = sort_t(T)
sekwens = sekwencja(P, T, len(P) - 1, len(T) - 1)
print(sekwens)