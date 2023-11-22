import numpy as np
import scipy
import pickle
import typing
import math
import types
import pickle 
from inspect import isfunction


from typing import Union, List, Tuple

def fun(x):
    return np.exp(-2*x)+x**2-1

def dfun(x):
    return -2*np.exp(-2*x) + 2*x

def ddfun(x):
    return 4*np.exp(-2*x) + 2


def bisection(a: Union[int,float], b: Union[int,float], f: typing.Callable[[float], float], epsilon: float, iteration: int) -> Tuple[float, int]:
    '''funkcja aproksymująca rozwiązanie równania f(x) = 0 na przedziale [a,b] metodą bisekcji.

    Parametry:
    a - początek przedziału
    b - koniec przedziału
    f - funkcja dla której jest poszukiwane rozwiązanie
    epsilon - tolerancja zera maszynowego (warunek stopu)
    iteration - ilość iteracji

    Return:
    float: aproksymowane rozwiązanie
    int: ilość iteracji
    '''


    if isinstance(a, (int, float)) and isinstance(b, (int, float)) and isinstance(epsilon, float) and isinstance(iteration, int):

        if f(a) * f(b) > 0:
            return None

        n = 0

        while n < iteration:
            c = (a + b) / 2
            if f(c) == 0 or abs(f(c)) <= abs(epsilon):
                return c, n
            n += 1

            if np.sign(f(a)) == np.sign(f(c)):
                a = c
            else:
                b = c
    else:
        return None


def secant(a: Union[int,float], b: Union[int,float], f: typing.Callable[[float], float], epsilon: float, iteration: int) -> Tuple[float, int]:
    '''funkcja aproksymująca rozwiązanie równania f(x) = 0 na przedziale [a,b] metodą siecznych.

    Parametry:
    a - początek przedziału
    b - koniec przedziału
    f - funkcja dla której jest poszukiwane rozwiązanie
    epsilon - tolerancja zera maszynowego (warunek stopu)
    iteration - ilość iteracji

    Return:
    float: aproksymowane rozwiązanie
    int: ilość iteracji
    '''
    if isinstance(a, (int, float)) and isinstance(b, (int, float)) and isinstance(epsilon, float) and isinstance(iteration, int) and callable(f):
        if f(a) * f(b) > 0:
            return None
        else:
            c = 0
            i = 0
            while i < iteration:
                c = b - f(b) * (b - a) / (f(b) - f(a))

                if f(a) * f(c) < 0:
                    b = c
                if f(b) * f(c) < 0:
                    a = c
                i += 1
                if abs(b - a) <= epsilon:
                    return c, i

            return c, i
    else:
        return None

secant(-5, 0.5, fun, 1e-10, 100)

def newton(f: typing.Callable[[float], float], df: typing.Callable[[float], float], ddf: typing.Callable[[float], float], a: Union[int,float], b: Union[int,float], epsilon: float, iteration: int) -> Tuple[float, int]:
    ''' Funkcja aproksymująca rozwiązanie równania f(x) = 0 metodą Newtona.
    Parametry: 
    f - funkcja dla której jest poszukiwane rozwiązanie
    df - pochodna funkcji dla której jest poszukiwane rozwiązanie
    ddf - druga pochodna funkcji dla której jest poszukiwane rozwiązanie
    a - początek przedziału
    b - koniec przedziału
    epsilon - tolerancja zera maszynowego (warunek stopu)
    Return:
    float: aproksymowane rozwiązanie
    int: ilość iteracji
    '''
    if all(callable(i) for i in [f, df, ddf]) and all(isinstance(i, (int, float)) for i in [a, b]) and isinstance(epsilon, float) and isinstance(iteration, int):
        przedzial = np.linspace(a, b, 1000)
        wartosci_df = df(przedzial)
        wartosci_ddf = ddf(przedzial)

        if not ((np.all(np.sign(wartosci_df) < 0) or np.all(np.sign(wartosci_df) > 0)) and (np.all(np.sign(wartosci_ddf) < 0) or np.all(np.sign(wartosci_ddf) > 0))):
            return None

        else:
            if f(a) * ddf(a) > 0:
                m = a
            else:
                m = b

        if f(a) * f(b) < 0:
            i = 0
            while i < iteration:
                result = m - f(m) / df(m)
                if np.abs(result - m) < epsilon:
                    return result, i
                if i == iteration - 1:
                    return result, iteration
                m = result
                i += 1
    return None



