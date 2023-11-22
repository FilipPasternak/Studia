import polska


class Vertex:
    def __init__(self, dane):
        self.ID = dane[2]
        self.x = dane[0]
        self.y = dane[1]

    def __hash__(self):
        return hash(self.ID)

    def __eq__(self, other):
        return self.ID == other.ID

    def __str__(self):
        return str(self.ID)

class MacierzSasiedztwa:
    def __init__(self):
        self.size = 0
        self.matrix = []
        self.VertexList = []

    def isEmpty(self):
        return self.order() == 0

    def order(self):
        return len(self.VertexList)

    def size(self):
        return self.size

    def insertVertex(self, vertex):
        old_order = self.order()
        self.VertexList.append(vertex)

        for i in range(old_order):
            self.matrix[i].append(0)
        self.matrix.append([0 for x in range(old_order + 1)])

    def getVertexIdx(self, vertex):
        for i in range(self.order()):
            if vertex == self.VertexList[i]:
                index = i
                return index
        return None

    def getVertex(self, idx):
        return self.VertexList[idx]

    def insertEdge(self, vertex1, vertex2, edge=1):
        if not (vertex1 in self.VertexList):
            self.insertVertex(vertex1)
        if not (vertex2 in self.VertexList):
            self.insertVertex(vertex2)

        index_1 = self.getVertexIdx(vertex1)
        index_2 = self.getVertexIdx(vertex2)
        self.matrix[index_1][index_2] = edge
        self.matrix[index_2][index_1] = edge

        self.size += 1

    def deleteVertex(self, vertex):
        idx = self.getVertexIdx(vertex)
        for i in range(self.order()):
            popped = self.matrix[i].pop(idx)
            if popped != 0:
                self.size -= 1

        self.matrix.pop(idx)
        self.VertexList.pop(self.getVertexIdx(vertex))

    def deleteEdge(self, vertex1, vertex2):
        index_1 = self.getVertexIdx(vertex1)
        index_2 = self.getVertexIdx(vertex2)

        self.matrix[index_1][index_2] = 0
        self.matrix[index_2][index_1] = 0

        self.size -= 1

    def edges(self):
        edges = []
        for i in range(self.order()):
            for j in range(self.order()):
                if self.matrix[i][j] != 0:
                    edge = (self.VertexList[i].ID, self.VertexList[j].ID)
                    edges.append(edge)
        return edges

    def __str__(self):
        s = ""
        for i in range(self.order()):
            s += str(self.matrix[i]) + '\n'
        return s

    def neighbours(self, index):
        neighbours = []
        for i in range(self.order()):
            if self.matrix[index][i] != 0:
                neighbour = self.VertexList[i]
                weight = self.matrix[index][i]
                neighbours.append((neighbour, weight))
        return neighbours


class ListaSasiedztwa:
    def __init__(self):
        self.size = 0
        self.list = []
        self.VertexList = []

    def isEmpty(self):
        return self.order() == 0

    def insertVertex(self, vertex):
        self.VertexList.append(vertex)
        self.list.append([])

    def getVertexIdx(self, vertex):
        for i in range(self.order()):
            if self.VertexList[i] == vertex:
                return i
        return None

    def insertEdge(self, vertex1, vertex2, edge = 1):
        if not (vertex1 in self.VertexList):
            self.insertVertex(vertex1)
        if not (vertex2 in self.VertexList):
            self.insertVertex(vertex2)

        index_1 = self.getVertexIdx(vertex1)
        index_2 = self.getVertexIdx(vertex2)

        self.list[index_1].append((vertex2, edge))
        self.list[index_2].append((vertex1, edge))

        self.size += 1

    def deleteVertex(self, vertex):
        for i in range(self.order()):
            j = 0
            for v, edge in self.list[i]:
                if v == vertex:
                    self.list[i].pop(j)
                    self.size -= 1
                j += 1

        self.list.pop(self.getVertexIdx(vertex))
        self.VertexList.pop(self.getVertexIdx(vertex))

    def deleteEdge(self, vertex1, vertex2):
        index_1 = self.getVertexIdx(vertex1)
        index_2 = self.getVertexIdx(vertex2)

        j = 0
        for v in self.VertexList[index_1]:
            if v == vertex2:
                self.list[index_1].pop(j)
            j += 1
        j = 0
        for v in self.VertexList[index_2]:
            if v == vertex1:
                self.list[index_2].pop(j)
            j += 1

        self.size -= 1

    def getVertex(self, index):
        return self.VertexList[index]

    def edges(self):
        edges = []
        for i in range(self.order()):
            for j in range(len(self.list[i])):
                edges.append((self.getVertex(i).ID, self.list[i][j][0].ID))
        return edges

    def order(self):
        return len(self.VertexList)

    def size(self):
        return self.size

    # def wage(self, vertex1, vertex2):
    #     edges = self.edges()
    #     for i in range(len(edges)):
    #         v1, v2, wage = edges[i]
    #         if v1 == vertex1 and v2 == vertex2:
    #             return wage
    #     return None

    def __str__(self):
        s = [[] for i in range(self.order())]
        for i in range(self.order()):
            for vertex, edge in self.list[i]:
                s[i].append((str(vertex), edge))
        return str(s)

    def neighbours(self, index):
        neighbours = []
        for i in range(len(self.list[index])):
            neighbour_index = self.getVertexIdx(self.list[index][i][0])
            weight = self.list[index][i][1]
            neighbours.append((neighbour_index, weight))
        return neighbours


def printGraph(g):
    n = g.order()
    print("------GRAPH------",n)
    for i in range(n):
        v = g.getVertex(i)
        print(v, end = " -> ")
        nbrs = g.neighbours(i)
        for (j, w) in nbrs:
            print(g.getVertex(j), w, end=";")
        print()
    print("-------------------")



if __name__ == "__main__":

    lista = polska.graf

    mapa = MacierzSasiedztwa()

    for litera1, litera2 in lista:
        v1 = Vertex(polska.slownik[litera1])
        v2 = Vertex(polska.slownik[litera2])

        mapa.insertEdge(v1, v2)

    polska.draw_map(mapa.edges())



    mapa = ListaSasiedztwa()

    for litera1, litera2 in lista:
        v1 = Vertex(polska.slownik[litera1])
        v2 = Vertex(polska.slownik[litera2])

        mapa.insertEdge(v1, v2)

    print(mapa.edges())

    polska.draw_map(mapa.edges())