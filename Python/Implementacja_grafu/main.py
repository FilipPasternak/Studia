import numpy as np


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
        self.order = 0
        self.matrix = np.zeros(1)
        self.VertexList = []

    def isEmpty(self):
        return self.order == 0

    def order(self):
        return self.order

    def size(self):
        return self.size

    def insertVertex(self, vertex):
        self.VertexList.append(vertex)
        if len(self.VertexList) > self.order:
            col = np.zeros(1, self.order)
            row = np.zeros(1, self.order+1)
            np.column_stack((self.matrix, col))
            self.matrix = np.r_[self.matrix, [row]]
            self.order += 1

    def insertEdge(self, vertex1, vertex2, edge = 1):
        if vertex1 in self.VertexList and vertex2 in self.VertexList:
            idx1 = hash(vertex1)
            idx2 = hash(vertex2)
            self.matrix[idx1][idx2], self.matrix[idx2][idx1] = edge

    def deleteVertex(self, vertex):
        idx = hash(vertex)

        for row in range(self.order):
            self.matrix[row].pop(idx)
        self.matrix.pop(idx)


class ListaSasiedztwa:
    def __init__(self):
        pass
