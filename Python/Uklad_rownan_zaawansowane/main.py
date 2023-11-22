import numpy as np
import scipy as sp
from scipy import linalg
from  datetime import datetime
import pickle

from typing import Union, List, Tuple

def spare_matrix_Abt(m: int,n: int):
    """Funkcja tworząca zestaw składający się z macierzy A (m,n), wektora b (m,)  i pomocniczego wektora t (m,) zawierających losowe wartości
    Parameters:
    m(int): ilość wierszy macierzy A
    n(int): ilość kolumn macierzy A
    Results:
    (np.ndarray, np.ndarray): macierz o rozmiarze (m,n) i wektorem (m,)
                Jeżeli dane wejściowe niepoprawne funkcja zwraca None
    """
    if (isinstance(m, int) and isinstance(n, int)) and (m > 0 and n > 0):
       t : np.ndarray = np.linspace(0, 1, m)
       b : np.ndarray = np.zeros((m, ))
       A : np.ndarray = np.fliplr(np.vander(t, N=n))
       for i in range(0, m):
        b[i] += np.cos(4*t[i])
    else:
        return None
    return A, b

def square_from_rectan(A: np.ndarray, b: np.ndarray):
    """Funkcja przekształcająca układ równań z prostokątną macierzą współczynników na kwadratowy układ równań. Funkcja ma zwrócić nową macierz współczynników  i nowy wektor współczynników
    Parameters:
      A: macierz A (m,n) zawierająca współczynniki równania
      b: wektor b (m,) zawierający współczynniki po prawej stronie równania
    Results:
    (np.ndarray, np.ndarray): macierz o rozmiarze (n,n) i wektorem (n,)
             Jeżeli dane wejściowe niepoprawne funkcja zwraca None
     """
    if isinstance(A, np.ndarray) and isinstance(b, np.ndarray):
        A_square = np.dot(np.transpose(A), A)
        b_square = np.dot(np.transpose(A), b)

        return A_square, b_square

    else:
        return None



def residual_norm(A: np.ndarray, x: np.ndarray, b: np.ndarray):
    """Funkcja obliczająca normę residuum dla równania postaci:
    Ax = b

      Parameters:
      A: macierz A (m,n) zawierająca współczynniki równania
      x: wektor x (n,) zawierający rozwiązania równania
      b: wektor b (m,) zawierający współczynniki po prawej stronie równania

      Results:
      (float)- wartość normy residuom dla podanych parametrów
      """
    if isinstance(A, np.ndarray) and (x, np.ndarray) and (x, np.ndarray):
          Ax = np.dot(A, np.transpose(x))
          residuum = b - Ax
          return np.linalg.norm(residuum)
    else:
      return None

