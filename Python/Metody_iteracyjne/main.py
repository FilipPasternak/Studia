import numpy as np
import scipy as sp
import pickle

from typing import Union, List, Tuple, Optional
import random

def diag_dominant_matrix_A_b(m: int) -> Tuple[np.ndarray, np.ndarray]:
    """Funkcja tworząca zestaw składający się z macierzy A (m,m), wektora b (m,) o losowych wartościach całkowitych z przedziału 0, 9
    Macierz A ma być diagonalnie zdominowana, tzn. wyrazy na przekątnej sa wieksze od pozostałych w danej kolumnie i wierszu
    Parameters:
    m int: wymiary macierzy i wektora
    
    Returns:
    Tuple[np.ndarray, np.ndarray]: macierz diagonalnie zdominowana o rozmiarze (m,m) i wektorem (m,)
                                   Jeżeli dane wejściowe niepoprawne funkcja zwraca None
    """

    if isinstance(m, int) and m > 0:
        diag = np.zeros((m, m))

# SPRAWDZANIE WIERSZY
        for i in range(len(diag)):
            for j in range(len(diag[i])):
                if j != i:
                    diag[i][j] = random.randrange(0, 10, 1)
# USTAWIANIE DIAGONALI
        for i in range(m):
            w_sum = 0
            for j in range(m):
                if j != i:
                    w_sum += diag[i][j]
                if j == m - 1:
                    diag[i][i] = w_sum + 1
# SPRAWDZANIE KOLUMN
        for i in range(m):
            val_diag = diag[i][i]
            sum_column = 0
            for j in range(m):
                if j != i:
                    sum_column += diag[j][i]

            if val_diag <= sum_column:
                diag[i][i] = sum_column + 1
        b = np.zeros(m)
        for i in range(m):
            b[i] = random.randrange(0, 9, 1)

        return diag, b

    else:
        return None

def is_diag_dominant(A: np.ndarray) -> bool:
    """Funkcja sprawdzająca czy macierzy A (m,m) jest diagonalnie zdominowana
    Parameters:
    A np.ndarray: macierz wejściowa
    
    Returns:
    bool: sprawdzenie warunku 
          Jeżeli dane wejściowe niepoprawne funkcja zwraca None
    """
    if isinstance(A, np.ndarray):
        if len(A) == 1 and len(A[0]) != 1:
            return None

        m, n = A.shape
        if m != n:
            return None

        for i in range(len(A)):
            diag_val = A[i][i]
            w_sum = 0
            c_sum = 0
            for j in range(len(A[i])):
                if i != j:
                    w_sum += A[i][j]
                    c_sum += A[j][i]
            if w_sum >= diag_val or c_sum >= diag_val:
                return False
        return True

def symmetric_matrix_A_b(m: int) -> Tuple[np.ndarray, np.ndarray]:
    """Funkcja tworząca zestaw składający się z macierzy A (m,m), wektora b (m,) o losowych wartościach całkowitych z przedziału 0, 9
    Parameters:
    m int: wymiary macierzy i wektora
    
    Returns:
    Tuple[np.ndarray, np.ndarray]: symetryczną macierz o rozmiarze (m,m) i wektorem (m,)
                                   Jeżeli dane wejściowe niepoprawne funkcja zwraca None
    """
    if isinstance(m, int) and m > 0:
        # UTWORZENIE b
        b = np.zeros(m)
        for i in range(m):
            b[i] = random.randrange(0, 9, 1)

        # UTWORZENIE A
        A = np.zeros((m, m))
        for i in range(m):
            for j in range(m):
                if j >= i:
                    A[j][i] = A[i][j] = random.randrange(0, 20, 1)
                else:
                    continue
        return A, b
    else:
        return None
print(symmetric_matrix_A_b(3))

def is_symmetric(A: np.ndarray) -> bool:
    """Funkcja sprawdzająca czy macierzy A (m,m) jest symetryczna
    Parameters:
    A np.ndarray: macierz wejściowa
    
    Returns:
    bool: sprawdzenie warunku 
          Jeżeli dane wejściowe niepoprawne funkcja zwraca None
    """
    if isinstance(A, np.ndarray):
        if len(A) == 1 and len(A[0]) != 1:
            return None

        m, n = A.shape
        if m != n:
            return None
        else:
            for i in range(m):
                for j in range(m):
                    if A[i][j] != A[j][i]:
                        return False
            return True
    else:
        return None


def solve_jacobi(A: np.ndarray, b: np.ndarray, x_init: np.ndarray,
                 epsilon: Optional[float] = 1e-8, maxiter: Optional[int] = 100) -> Tuple[np.ndarray, int]:
    """Funkcja tworząca zestaw składający się z macierzy A (m,m), wektora b (m,) o losowych wartościach całkowitych
    Parameters:
    A np.ndarray: macierz współczynników
    b np.ndarray: wektor wartości prawej strony układu
    x_init np.ndarray: rozwiązanie początkowe
    epsilon Optional[float]: zadana dokładność
    maxiter Optional[int]: ograniczenie iteracji
    
    Returns:
    np.ndarray: przybliżone rozwiązanie (m,)
                Jeżeli dane wejściowe niepoprawne funkcja zwraca None
    int: iteracja
    """
    if isinstance(A, np.ndarray) and isinstance(b, np.ndarray) and isinstance(x_init, np.ndarray) and isinstance(epsilon, float) and isinstance(maxiter, int):

        m, n  = A.shape
        if m != n:
            return None
        if b.size != m or x_init.size != m:
            return None
        if epsilon <= 0 or maxiter <= 0:
            return None


        D = np.diag(np.diag(A))
        LU = A - D
        x = x_init
        D_inv = np.diag(1 / np.diag(D))
        resid = []
        iterations = 0
        for i in range(maxiter):
            x_new = np.dot(D_inv, b - np.dot(LU, x))
            r_norm = np.linalg.norm(x_new - x)
            resid.append(r_norm)
            if r_norm < epsilon:
                return x_new, resid
            x = x_new
            iterations += 1
        return x, iterations
    else:
        return None


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