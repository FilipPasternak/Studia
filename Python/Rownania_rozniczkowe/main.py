import numpy as np
from typing import Union, Callable


def solve_euler(fun: Callable, t_span: np.array, y0: np.array):
    '''
    Funkcja umożliwiająca rozwiązanie układu równań różniczkowych z wykorzystaniem metody Eulera w przód.

    Parameters:
    fun: Prawa strona równania. Podana funkcja musi mieć postać fun(t, y).
    Tutaj t jest skalarem i istnieją dwie opcje dla ndarray y: Może mieć kształt (n,); wtedy fun musi zwrócić array_like z kształtem (n,).
    Alternatywnie może mieć kształt (n, k); wtedy fun musi zwrócić tablicę typu array_like z kształtem (n, k), tj. każda kolumna odpowiada jednej kolumnie w y.
    t_span: wektor czasu dla którego ma zostać rozwiązane równanie
    y0: warunke początkowy równanai o wymiarze (n,)
    Results:
    (np.array): macierz o wymiarze (n,m) zawierająca w wkolumnach kolejne rozwiązania fun w czasie t_span.

    '''

    n = np.transpose(y0)
    y = np.zeros((np.shape(y0)[0], np.shape(t_span)[0]))
    y[:,0] = n
    for i in range(1, len(t_span)):
        n1 = n + (t_span[i] - t_span[i - 1]) * np.transpose(fun(n, t_span[i]))
        y[:, i] = n1
        n = n1
    return y

