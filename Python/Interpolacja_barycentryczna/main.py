##
import numpy as np
import scipy
import pickle
import matplotlib.pyplot as plt

from typing import Union, List, Tuple

def chebyshev_nodes(n:int=10)-> np.ndarray:
    """Funkcja tworząca wektor zawierający węzły czybyszewa w postaci wektora (n+1,)
    
    Parameters:
    n(int): numer ostaniego węzła Czebyszewa. Wartość musi być większa od 0.
     
    Results:
    np.ndarray: wektor węzłów Czybyszewa o rozmiarze (n+1,). 
                Jeżeli dane wejściowe niepoprawne funkcja zwraca None
    """
    if (not isinstance(n, int)) or n <= 0:
        return None

    else:
        nodes = np.zeros(n+1)

        for k in range (0, n+1):
            nodes[k] = np.cos((k*np.pi) / n)
        return nodes
    
def bar_czeb_weights(n:int=10)-> np.ndarray:
    """Funkcja tworząca wektor wag dla węzłów czybyszewa w postaci (n+1,)
    
    Parameters:
    n(int): numer ostaniej wagi dla węzłów Czebyszewa. Wartość musi być większa od 0.
     
    Results:
    np.ndarray: wektor wag dla węzłów Czybyszewa o rozmiarze (n+1,). 
                Jeżeli dane wejściowe niepoprawne funkcja zwraca None
    """

    if isinstance(n, int) and n > 0:
        nodes = chebyshev_nodes(n)
        w = np.zeros((len(nodes)))

        for i in range(w.size):
            if i == 0 or i == w.size - 1:
                w[i] = ((-1)**i)/2
            else:
                w[i] = (-1)**i
        return w
    else:
        return None

f1 = lambda x: np.sign(x)*x + x**2
f2 = lambda x: np.sign(x) * x**2
f3 = lambda x: np.absolute(np.sin(5*x))**3
f4_a = lambda x: 1/(1+x**2)
f4_b = lambda x: 1/(1+(25*x**2))
f4_c = lambda x: 1/(1+(100*x**2))
f5 = lambda x: np.sign(x)

def  barycentric_inte(xi:np.ndarray,yi:np.ndarray,wi:np.ndarray,x:np.ndarray)-> np.ndarray:
    """Funkcja przprowadza interpolację metodą barycentryczną dla zadanych węzłów xi
        i wartości funkcji interpolowanej yi używając wag wi. Zwraca wyliczone wartości
        funkcji interpolującej dla argumentów x w postaci wektora (n,) gdzie n to dłógość
        wektora n. 
    
    Parameters:
    xi(np.ndarray): węzły interpolacji w postaci wektora (m,), gdzie m > 0
    yi(np.ndarray): wartości funkcji interpolowanej w węzłach w postaci wektora (m,), gdzie m>0
    wi(np.ndarray): wagi interpolacji w postaci wektora (m,), gdzie m>0
    x(np.ndarray): argumenty dla funkcji interpolującej (n,), gdzie n>0 
     
    Results:
    np.ndarray: wektor wartości funkcji interpolujący o rozmiarze (n,). 
                Jeżeli dane wejściowe niepoprawne funkcja zwraca None
    """
    if isinstance(xi, np.ndarray) and isinstance(yi, np.ndarray) and isinstance(wi, np.ndarray) and isinstance(x, np.ndarray):
        if xi.shape == yi.shape and yi.shape == wi.shape:
            Y = []
            for x in np.nditer(x):
                L = wi/(x - xi)
                Y.append(yi @ L / sum(L))
            Y = np.array(Y)
            return Y
    else:
        return None

def L_inf(xr:Union[int, float, List, np.ndarray],x:Union[int, float, List, np.ndarray])-> float:
    """Obliczenie normy  L nieskończonośćg. 
    Funkcja powinna działać zarówno na wartościach skalarnych, listach jak i wektorach biblioteki numpy.
    
    Parameters:
    xr (Union[int, float, List, np.ndarray]): wartość dokładna w postaci wektora (n,)
    x (Union[int, float, List, np.ndarray]): wartość przybliżona w postaci wektora (n,1)
    
    Returns:
    float: wartość normy L nieskończoność,
                                    NaN w przypadku błędnych danych wejściowych
    """

    if isinstance(xr, (int, float, List, np.ndarray)) and isinstance(x, (int, float, List, np.ndarray)):

        if isinstance(xr, (int, float)) and isinstance(x, (List, np.ndarray)):
            return np.NaN
        if isinstance(x, (int, float)) and isinstance(xr, (List, np.ndarray)):
            return np.NaN


        if isinstance(xr, List) and isinstance(x, List):
            if len(xr) != len(x):
                return np.NaN
            else:
                answer = np.zeros(len(xr))
                for i in range(len(xr)):
                    answer[i] = np.absolute((xr[i] - x[i]))
                return np.max(answer)

        if isinstance(xr, np.ndarray) and isinstance(x, np.ndarray):
            if xr.shape != x.shape:
                return np.NaN
            else:
                answer = np.zeros(len(xr))
                for i in range(len(xr)):
                    answer[i] = np.absolute((xr[i] - x[i]))

            return np.max(answer)

        else:
            return np.absolute(xr - x)

    else:
        return np.NaN

x = np.linspace(-5, 5, 1000)
f_jedn = f2
f_trzyk = f3
y_jedn = f_jedn(x)
y_trzyk = f_trzyk(x)

xch = chebyshev_nodes(len(x) - 1)
wi = bar_czeb_weights(len(x) - 1)

print(type(xch), type(f_jedn(x)), type(wi), type(x))

f_jedn_inter = barycentric_inte(xch, f_jedn(x), wi, x)