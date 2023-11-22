class Vertex:
    def __init__(self, ID):
        self.ID = ID

    def __hash__(self):
        return hash(self.ID)

    def __eq__(self, other):
        return self.ID == other.ID


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
                    edge = hash(self.VertexList[i]), hash(self.VertexList[j])
                    edges.append(edge)
        return edges

    def __str__(self):
        s = ""
        for i in range(self.order()):
            s += str(self.matrix[i]) + '\n'
        return s


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

    def insertEdge(self, vertex1, vertex2):
        if not (vertex1 in self.VertexList):
            self.insertVertex(vertex1)
        if not (vertex2 in self.VertexList):
            self.insertVertex(vertex2)

        index_1 = self.getVertexIdx(vertex1)
        index_2 = self.getVertexIdx(vertex2)

        self.list[index_1].append(vertex2)
        self.list[index_2].append(vertex1)

        self.size += 1

    def deleteVertex(self, vertex):
        for i in range(self.order()):
            j = 0
            for v in self.list[i]:
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
                edges.append((hash(self.getVertex(i)), hash(self.list[i][j])))
        return edges

    def order(self):
        return len(self.VertexList)

    def size(self):
        return self.size

    def __str__(self):
        s = [[] for i in range(self.order())]
        for i in range(self.order()):
            for j in range(len(self.list[i])):
                s[i].append(hash(self.list[i][j]))
        return str(s)


vertex1 = Vertex(1)
vertex2 = Vertex(2)
vertex3 = Vertex(3)
vertex4 = Vertex(4)

matrix = ListaSasiedztwa()
matrix.insertVertex(vertex1)
matrix.insertVertex(vertex2)
matrix.insertVertex(vertex3)
matrix.insertVertex(vertex4)

matrix.insertEdge(vertex2, vertex1)
matrix.insertEdge(vertex3, vertex1)
matrix.insertEdge(vertex2, vertex3)

print(matrix.edges())

print(matrix)

matrix.deleteVertex(vertex3)

print(matrix.edges())

print(matrix)