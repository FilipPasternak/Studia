

class Element:
    def __init__(self, data, key):
        self.data = data
        self.key = key



class Mieszana:
    def __init__(self, size, c1 = 1, c2 = 0):
        self.size = size
        self.c1 = c1
        self.c2 = c2
        self.memory = 0
        self.tab = [Element(None, None) for i in range(size)]


    def funkcja_mieszajaca(self, key):
        if isinstance(key, str):
            key_str = 0
            for l in key:
                key_str += ord(l)
            return key_str % self.size
        else:
            return key % self.size

    def search(self, key):
        for element in self.tab:
            if element.key == key:
                return element.data
        else:
            return None

    def insert(self, data, key):
        indeks = self.funkcja_mieszajaca(key)

        if self.tab[indeks].key is None:
            self.tab[indeks] = Element(data, key)

        else:
            znalezione = False
            if self.tab[indeks].key == key:
                self.tab[indeks].data = data
            else:
                for i in range(1, self.size + 1):
                    nowy_indeks = (indeks + (self.c1 * i) + (self.c2 * i ** 2)) % self.size

                    if (self.tab[nowy_indeks] is None) or (self.tab[nowy_indeks].key is None):
                        self.tab[nowy_indeks] = Element(data, key)
                        znalezione = True
                        break

                if not znalezione:
                    print("Brak pamieci \n")

    def remove(self, key):
        indeks = self.funkcja_mieszajaca(key)
        self.tab[indeks] = Element(None, None)

    def __str__(self):
        string = ""
        for element in self.tab:
            if element.key is None:
                string += "None\n"
            else:
                string += '{' + f'{element.key}' + ':' + f'{element.data}' + '}\n'
        return string

keys1 = [1,2,3,4,5,18,31,8,9,10,11,12,13,14,15]
values1 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O']

def func1(keys, values, c1 = 1, c2 = 0):
    hash = Mieszana(13, c1, c2)

    for i in range(len(values)):
        hash.insert(values[i], keys[i])

    print(hash)

    print(hash.search(5), '\n')
    print(hash.search(14), '\n')

    hash.insert('Z', 5)

    print(hash.search(5), '\n')

    hash.remove(5)

    print(hash)

    print(hash.search(31), '\n')

keys2 = []
for i in range(len(values1)):
    keys2.append(13**(i+1))

def func2(keys, values, c1 = 1, c2 = 0):
    hash = Mieszana(13, c1, c2)
    for i in range(len(values)):
        hash.insert(values[i], keys[i])
    print(hash, '\n')

func1(keys1, values1)
func2(keys2, values1)

func2(keys2, values1, 0, 1)
func1(keys1, values1, 0, 1)
