
class Kolejka:
    def __init__(self, size = 5):
        self.elements = [None for i in range(size)]
        self.size = size
        self.odczyt = 0
        self.zapis = 0

    def is_empty(self):
        if self.odczyt == self.zapis:
            return True
        else:
            return False

    def peek(self):
        return self.elements[self.odczyt]

    def dequeue(self):
        if self.elements[self.odczyt]:
            element = self.elements[self.odczyt]
            self.elements[self.odczyt] = None
            if self.odczyt < self.size - 1:
                self.odczyt += 1
            else:
                self.odczyt = 0
            return element
        else:
            return None

    def realloc(self, size):
        oldSize = self.size
        return [self.elements[i] if i < oldSize else None for i in range(size)]


    def enqueue(self, data):
        if self.zapis == self.odczyt and self.odczyt:
            self.elements = self.realloc(self.size * 2)
            OldSize = self.size
            self.size = self.size * 2

            for i in range(self.size):
                if i < self.odczyt:
                    continue
                elif OldSize > i >= self.odczyt:
                    self.elements[i + OldSize] = self.elements[i]
                    self.elements[i] = None
            self.odczyt += OldSize
            self.elements[self.zapis] = data
            self.zapis += 1

        elif self.zapis < self.size - 1:
            self.elements[self.zapis] = data
            self.zapis += 1
        else:
            self.elements[self.zapis] = data
            self.zapis = 0

    def __str__(self):
        napis = ''
        first_element = True
        odczyt_str = self.odczyt
        zapis_str = self.zapis
        while odczyt_str != zapis_str:
            if self.elements[odczyt_str]:

                if first_element:
                    napis += "[ "
                    first_element = False

                napis += str(self.elements[odczyt_str]) + " "

                if odczyt_str == self.size - 1:
                    odczyt_str = 0
                else:
                    odczyt_str += 1

        if not self.is_empty():
            napis += ']\n'
        if self.is_empty():
            return '[]'

        return napis

if __name__ == "__main__":
    queue = Kolejka()                   #Utworzenie pustej kolejki

    for i in range(1, 5):
        queue.enqueue(i)                #Dodanie do kolejki elementow

    print(queue.dequeue(), '\n')        #wypisanie i usuniecie pierwszego elementu z kolejki

    print(queue.peek(), '\n')           #Uzycie peek do wypisania drugiej danej

    print(queue)                        #Wypisanie kolejki

    for i in range(5, 9):
        queue.enqueue(i)                #Dodanie do kolejki nastepnych elementow (uzycie funkcji realloc)

    print(queue)                        #Wypisanie kolejki

    while queue.peek():
        print(queue.dequeue())          #Usuniecie kazdego elementu z kolejki

    print(queue)                        #Wypisanie pustej kolejki