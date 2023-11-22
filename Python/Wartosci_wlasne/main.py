import numpy as np
import scipy as sp
from scipy import linalg
from  datetime import datetime
import pickle

from typing import Union, List, Tuple

'''
Do celów testowych dla elementów losowych uzywaj seed = 24122022
'''

def random_matrix_by_egval(egval_vec: np.ndarray):
    """Funkcja z pierwszego zadania domowego
    Parameters:
    egval_vec : wetkor wartości własnych
    Results:
    np.ndarray: losowa macierza o zadanych wartościach własnych 
                Jeżeli dane wejściowe niepoprawne funkcja zwraca None
    """

    if isinstance(egval_vec, np.ndarray) or isinstance(egval_vec, List):
        np.random.seed(24122022)

        for i in range(len(egval_vec)):
            if isinstance(egval_vec[i], str):
                return None
        J = np.zeros((len(egval_vec), len(egval_vec)))

        for i in range(len(egval_vec)):
            if isinstance(egval_vec[i], complex):
                J = np.zeros((len(egval_vec), len(egval_vec)), dtype=complex)


        for i in range(len(J)):
            J[i][i] = egval_vec[i]

        P = np.random.rand(len(egval_vec), len(egval_vec))
        P_inv = np.linalg.inv(P)

        return np.dot(np.dot(P, J), P_inv)
    else:
        return None


def frob_a(coef_vec: np.ndarray):
    """Funkcja z drugiego zadania domowego
    Parameters:
    coef_vec : wetkor wartości wspołczynników
    Results:
    np.ndarray: macierza Frobeniusa o zadanych wartościach współczynników wielomianu 
                Jeżeli dane wejściowe niepoprawne funkcja zwraca None
    """
    if isinstance(coef_vec, np.ndarray) or isinstance(coef_vec, List):

        for i in range(len(coef_vec)):
            if isinstance(coef_vec[i], str):
                return None

        frob = np.zeros((len(coef_vec), len(coef_vec)))
        for i in range(len(coef_vec)):
            if i == len(coef_vec) - 1:
                for j in range(len(coef_vec)):
                    frob[i][j] = -coef_vec[len(coef_vec) - j - 1]
            else:
                for j in range(len(coef_vec)):
                    if j == i+1:
                        frob[i][j] = 1
                    else:
                        continue

        return frob
    else:
        return None
    
def polly_from_egval(egval_vec: np.ndarray):
    """Funkcja z laboratorium 8
    Parameters:
    egval_vec: wetkor wartości własnych
    Results:
    np.ndarray: wektor współczynników wielomianu charakterystycznego
                Jeżeli dane wejściowe niepoprawne funkcja zwraca None
    """

    return np.polynomial.polynomial.polyfromroots(egval_vec)