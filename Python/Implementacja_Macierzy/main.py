

class Macierz:

    def __init__(self, vals, parametr = 0):

        if isinstance(vals, list):
            self.matrix = vals

        elif isinstance(vals, tuple):
            rows, cols = vals
            wynik = []
            for i in range(rows):
                wynik.append([parametr])
            for i in range(cols - 1):
                for j in range(rows):
                    wynik[j].append(parametr)
            self.matrix = wynik

        else:
            print("Bledne wprowadzenie danych")

    def __add__(self, other):
        if self.size() != other.size():
            print('Wymiary macierzy niezgodne - brak mozliwosci wykonania dzialania')
        else:
            result = Macierz((self.size()))
            rows, cols = self.size()
            for i in range(rows):
                for j in range(cols):
                    result[i][j] = self.matrix[i][j] + other.matrix[i][j]
            return result

    def __mul__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            rows, cols = self.size()
            result = Macierz((rows, cols))
            for i in range(rows):
                for j in range(cols):
                    result[i][j] = self[i][j] * other
            return result
        if isinstance(other, Macierz):
            rows_self, cols_self = self.size()
            rows_other, cols_other = other.size()
            if cols_self != rows_other:
                print('Wymiary macierzy niezgodne - brak mozliwosci wykonania dzialania')
            else:
                result = Macierz((rows_self, cols_other))
                for i in range(rows_self):
                    for j in range(cols_other):     #glowna petla

                        for k in range(rows_other):
                            result[i][j] += self[i][k] * other[k][j]
                return result

    def __getitem__(self, item):
        return self.matrix[item]

    def size(self):
        return len(self.matrix), len(self.matrix[0])

    def __str__(self):
        rows, cols = self.size()
        result = ''
        for i in range(rows):
            result += '| '
            for j in range(cols):
                result += str(self[i][j]) + ' '
            result += '|\n'
        return result

def transpose(matrix: Macierz):
    rows, cols = matrix.size()
    result = Macierz((cols, rows))

    for i in range(rows):
        for j in range(cols):
            result[j][i] = matrix[i][j]
    return result

m1 = Macierz(
[ [1, 0, 2],
  [-1, 3, 1] ]
)

print(transpose(m1))

m2 = Macierz((2, 3), 1)

print(m1 + m2)

m3 = Macierz(
[ [3, 1],
  [2, 1],
  [1, 0]]
)

print(m1 * m3)



