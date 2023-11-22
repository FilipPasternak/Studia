import numpy as np
import random

from typing import Union

def random_matrix_Ab(m:int):
    """Funkcja tworząca zestaw składający się z macierzy A (m,m) i wektora b (m,)  zawierających losowe wartości
    Parameters:
    m(int): rozmiar macierzy
    Results:
    (np.ndarray, np.ndarray): macierz o rozmiarze (m,m) i wektorem (m,)
                Jeżeli dane wejściowe niepoprawne funkcja zwraca None
    """
    if not isinstance(m, int):
        return None

    elif m <= 0:
        return None

    else:

        A = np.zeros((m, m))
        b = np.zeros(m)

        for i in range(m):
            for j in range(m):
                A[i][j] = random.randint(0, 100)

        for i in range(m):
            b[i] = random.randint(0, 100)
        return A, b

def residual_norm(A:np.ndarray,x:np.ndarray, b:np.ndarray):
    """Funkcja obliczająca normę residuum dla równania postaci:
    Ax = b

      Parameters:
      A: macierz A (m,m) zawierająca współczynniki równania 
      x: wektor x (m.) zawierający rozwiązania równania 
      b: wektor b (m,) zawierający współczynniki po prawej stronie równania

      Results:
      (float)- wartość normy residuom dla podanych parametrów"""
    if all(isinstance(i, np.ndarray) for i in [A, x, b]):

      if x.shape == b.shape and A.shape[1] == A.shape[0]:

        Ax = A @ np.transpose(x)
        residuum = b - Ax
        return np.linalg.norm(residuum)

      else:
        return None

    else:
      return None


def log_sing_value(n:int, min_order:Union[int,float], max_order:Union[int,float]):
    """Funkcja generująca wektor wartości singularnych rozłożonych w skali logarytmiczne
    
        Parameters:
         n(np.ndarray): rozmiar wektora wartości singularnych (n,), gdzie n>0
         min_order(int,float): rząd najmniejszej wartości w wektorze wartości singularnych
         max_order(int,float): rząd największej wartości w wektorze wartości singularnych
         #Results:
         np.ndarray - wektor nierosnących wartości logarytmicznych o wymiarze (n,) zawierający wartości logarytmiczne na zadanym przedziale
         """
    if not (isinstance(n, int) and isinstance(min_order, (int, float)) and isinstance(max_order, (int, float))):
        return None

    else:
        if n <= 0:
            return None

        if max_order < min_order:
            return None


        else:
            s = np.logspace(max_order, min_order, num=n)
            return s


def order_sing_value(n:int, order:Union[int,float] = 2, site:str = 'gre'):
    """Funkcja generująca wektor losowych wartości singularnych (n,) będących wartościami zmiennoprzecinkowymi losowanymi przy użyciu funkcji np.random.rand(n)*10. 
        A następnie ustawiająca wartość minimalną (site = 'low') albo maksymalną (site = 'gre') na wartość o  10**order razy mniejszą/większą.
    
        Parameters:
        n(np.ndarray): rozmiar wektora wartości singularnych (n,), gdzie n>0
        order(int,float): rząd przeskalowania wartości skrajnej
        site(str): zmienna wskazująca stronnę zmiany:
            - site = 'low' -> sing_value[-1] * 10**order
            - site = 'gre' -> sing_value[0] * 10**order
        
        Results:
        np.ndarray - wektor wartości singularnych o wymiarze (n,) zawierający wartości logarytmiczne na zadanym przedziale
        """


    if isinstance(n, int) and isinstance(order, (int, float)) and (site == 'low' or 'gre'):

        if n <= 0 or order <= 0:
            return None

        sing_value = np.random.rand(n)*10

        if site == 'low':
            sing_value[-1] = sing_value[-1] * 10**order
            return sing_value
        if site == 'gre':
            sing_value[0] = sing_value[0] * 10 ** order
            return sing_value
        else:
            return None

    else:
        return None



def create_matrix_from_A(A:np.ndarray, sing_value:np.ndarray):
    """Funkcja generująca rozkład SVD dla macierzy A i zwracająca otworzenie macierzy A z wykorzystaniem zdefiniowanego wektora warości singularnych

            Parameters:
            A(np.ndarray): rozmiarz macierzy A (m,m)
            sing_value(np.ndarray): wektor wartości singularnych (m,)


            Results:
            np.ndarray: macierz (m,m) utworzoną na podstawie rozkładu SVD zadanej macierzy A z podmienionym wektorem wartości singularnych na wektor sing_valu """
    if isinstance(A, np.ndarray) and isinstance(sing_value, np.ndarray):
        m, n = A.shape

        if m != n:
            return None

        if m != len(sing_value):
            return None

        else:
            U, S, V = np.linalg.svd(A)
            return np.dot(U * sing_value, V)

    else:
        return None
