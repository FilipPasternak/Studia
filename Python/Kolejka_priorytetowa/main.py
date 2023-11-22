import random
import time

class Element:
    def __init__(self, dane, priorytet: int):
        self.__dane = dane
        self.__priorytet = priorytet

    def __str__(self):
        return str(self.__priorytet) + ' : ' + str(self.__dane)

    def __lt__(self, other):
        if self.__priorytet < other.__priorytet:
            return True
        else:
            return False

    def __le__(self, other):
        if self.__priorytet <= other.__priorytet:
            return True
        else:
            return False

    def __ge__(self, other):
        if self.__priorytet >= other.__priorytet:
            return True
        else:
            return False

    def __gt__(self, other):
        if self.__priorytet > other.__priorytet:
            return True
        else:
            return False

    def __eq__(self, other):
        if self.__priorytet == other.__priorytet:
            return True
        else:
            return False

class Queue:
    def __init__(self, to_be_sorted = None):
        self.tab = []
        self.size = 0
        if to_be_sorted:
            self.tab = to_be_sorted
            self.size = len(to_be_sorted)
            for i in range(self.size):
                self.heapify_up(i)

    def sort(self):
        while self.size != 0:
            self.dequeue()
        return self.tab

    def print_sorted(self):
        print('{', end=' ')
        print(*self.tab[:len(self.tab)], sep=', ', end=' ')
        print('}')

    def is_empty(self):
        if self.size == 0:
            return True
        else:
            return False

    def peek(self):
        if not self.is_empty():
            return self.tab[0]
        else:
            return None

    def enqueue(self, element):
        if self.size == len(self.tab):
            self.tab.append(element)
        else:
            self.tab[self.size] = element

        self.size += 1
        self.heapify_up(self.size - 1)

    def dequeue(self):
        if self.is_empty():
            raise Exception('Kolejka jest pusta')

        root = self.tab[0]
        self.tab[0] = self.tab[self.size - 1]
        self.tab[self.size - 1] = root
        self.size -= 1

        if self.size > 0:
            self.heapify_down(0)

        return root

    def heapify_up(self, i):
        while i > 0 and self.tab[i] > self.tab[self.parent(i)]:
            self.tab[i], self.tab[self.parent(i)] = self.tab[self.parent(i)], self.tab[i]
            i = self.parent(i)

    def heapify_down(self, i):
        while self.left(i) < self.size:
            child = self.left(i)

            if self.right(i) < self.size and self.tab[self.right(i)] > self.tab[child]:
                child = self.right(i)

            if self.tab[i] < self.tab[child]:
                self.tab[i], self.tab[child] = self.tab[child], self.tab[i]
                i = child
            else:
                break


    def left(self, index):
        return 2 * index + 1

    def right(self, index):
        return 2 * (index + 1)

    def parent(self, index):
        if index % 2 == 0:
            return (index // 2) - 1
        else:
            return (index - 1) // 2

    def print_tab(self):
        if self.is_empty():
            print('{}')
        else:
            print('{', end=' ')
            print(*self.tab[:self.size], sep=', ', end=' ')
            print('}')

    def print_tree(self, idx, lvl):
        if idx<self.size:
            self.print_tree(self.right(idx), lvl+1)
            print(2*lvl*'  ', self.tab[idx] if self.tab[idx] else None)
            self.print_tree(self.left(idx), lvl+1)

    def selection_sort_swap(self):
        n = self.size
        for i in range(n):
            min_idx = i
            for j in range(i+1, n):
                if self.tab[j] < self.tab[min_idx]:
                    min_idx = j
            self.tab[i], self.tab[min_idx] = self.tab[min_idx], self.tab[i]

    def selection_sort_shift(self):
        n = self.size
        for i in range(n):
            min_idx = i
            for j in range(i+1, n):
                if self.tab[j] < self.tab[min_idx]:
                    min_idx = j
            min_element = self.tab.pop(min_idx)
            self.tab.insert(i, min_element)

    def test_sorting(self):
        # Generowanie 10 000 losowych liczb
        array = [random.randint(0, 99) for _ in range(10000)]

        # Sortowanie przez wybieranie (swap)
        start_time = time.time()
        self.tab = array.copy()
        self.size = len(self.tab)
        self.selection_sort_swap()
        end_time = time.time()
        print("Czas sortowania przez wybieranie (swap):", end_time - start_time)

        # Sortowanie przez wybieranie (shift)
        start_time = time.time()
        self.tab = array.copy()
        self.size = len(self.tab)
        self.selection_sort_shift()
        end_time = time.time()
        print("Czas sortowania przez wybieranie (shift):", end_time - start_time)

lista = [(5,'A'), (5,'B'), (7,'C'), (2,'D'), (5,'E'), (1,'F'), (7,'G'), (5,'H'), (1,'I'), (2,'J')]

to_be_sorted = []

for i in range(len(lista)):
    priorytet, data = lista[i]
    elem = Element(data, priorytet)
    to_be_sorted.append(elem)

q = Queue(to_be_sorted)

q.print_tab()

q.print_tree(0, 0)

q.sort()

q.print_sorted()

print("Sortowanie nie jest stabilne")

print('\n\n')


#test 2
to_be_sorted1 = []
for i in range(10000):
    to_be_sorted1.append(random.randint(0, 99))

t_start = time.perf_counter()
q1 = Queue(to_be_sorted1)
q1.sort()
q1.print_sorted()
t_stop = time.perf_counter()
print("Czas obliczeń:", "{:.7f}".format(t_stop - t_start))

print('\n\n')
# 2.

data = [(5,'A'), (5,'B'), (7,'C'), (2,'D'), (5,'E'), (1,'F'), (7,'G'), (5,'H'), (1,'I'), (2,'J')]

elements = [Element(dane, priorytet) for priorytet, dane in data]

q = Queue(elements.copy())
q.selection_sort_swap()
sorted_elements_swap = q.tab

q = Queue(elements.copy())
q.selection_sort_shift()
sorted_elements_shift = q.tab

print("Sortowanie przez zamianę miejscami (swap):")
for element in sorted_elements_swap:
    print(element)

print()

print("Sortowanie przez przesunięcie elementów (shift):")
for element in sorted_elements_shift:
    print(element)

print('\n\n')


# Test 2

q.test_sorting()