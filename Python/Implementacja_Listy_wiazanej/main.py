
class Element:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next


class ListaWiazana:
    def __init__(self):
        self.head = None

    def destroy(self):
        self.head = None

    def add(self, data):
        nowy_elem = Element(data)
        if self.head:
            nowy_elem.next = self.head
            self.head = nowy_elem
        else:
            self.head = nowy_elem

    def append(self, data):
        nowy_elem = Element(data)
        if self.head:
            aktualne = self.head
            while aktualne.next:
                aktualne = aktualne.next
            aktualne.next = nowy_elem
        else:
            self.head = nowy_elem

    def remove(self):
        if self.head:
            self.head = self.head.next
        else:
            print('Lista jest juz pusta')

    def remove_end(self):
        if self.head:
            aktualne = self.head
            while aktualne.next.next:
                aktualne = aktualne.next
            aktualne.next = None
        else:
            print('Lista jest juz pusta')

    def is_empty(self):
        if self.head:
            return False
        else:
            return True

    def length(self):
        if self.head:
            aktualne = self.head
            length = 1
            while aktualne.next:
                aktualne = aktualne.next
                length += 1
            return length
        else:
            return 0

    def get(self):
        return self.head.data

    def printLL(self):
        if self.head:
            aktualne = self.head
            while aktualne:
                print("-> ", aktualne.data)
                aktualne = aktualne.next




if __name__ == "__main__":
    lista_uczelni = [('AGH', 'Kraków', 1919),
    ('UJ', 'Kraków', 1364),
    ('PW', 'Warszawa', 1915),
    ('UW', 'Warszawa', 1915),
    ('UP', 'Poznań', 1919),
    ('PG', 'Gdańsk', 1945)]

    lista_uczelni_wiazana = ListaWiazana()     #Utworzenie listy

    for uczelnia in lista_uczelni:
        lista_uczelni_wiazana.append(uczelnia)  #Dodanie nazw uczelni do listy

    lista_uczelni_wiazana.printLL()             #Wypisanie listy

    print(lista_uczelni_wiazana.length())       #Wypisanie dlugosci listy

    lista_uczelni_wiazana.remove()              #Usuniecie pierwszego elementu

    print(lista_uczelni_wiazana.get())          #Wypisanie pierwszego elementu

    lista_uczelni_wiazana.remove_end()          #Usuniecie ostatniego elementu

    lista_uczelni_wiazana.printLL()             #Wypisanie listy

    lista_uczelni_wiazana.destroy()             #Usuniecie listy

    print(lista_uczelni_wiazana.is_empty())     #Sprawdzenie czy lista jest pusta

    lista_uczelni_wiazana.remove()              #Usuwanie pierwszego elementu z pustej listy

    lista_uczelni_wiazana.remove_end()          #Usuwanie ostatniego elementu z pustej listy
