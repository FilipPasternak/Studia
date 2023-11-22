
class Root:
    def __init__(self, root_node):
        self.root = root_node

class TreeNode:

    def __init__(self, key, data):
        self.key = key
        self.data = data
        self.left_node = None
        self.right_node = None
        self.root = None

    def search(self, key):
        if self.key is None or self.key == key:
            return self.data
        else:
            if key < self.key:
                if self.left_node.key is None:
                    return None
                else:
                    return self.left_node.search(key)

            if key > self.key:
                if self.right_node.key is None:
                    return None
                else:
                    return self.right_node.search(key)

    def insert(self, key, data, isroot = True):
        if self.key is None or self.key == key:
            self.key = key
            self.data = data
            if isroot:
                self.root = self
        else:
            if key < self.key:
                if self.left_node is None:
                    self.left_node = TreeNode(key, data)
                    self.left_node.root = self.root
                else:
                    self.left_node.insert(key, data, False)

            if key > self.key:
                if self.right_node is None:
                    self.right_node = TreeNode(key, data)
                    self.right_node.root = self.root
                else:
                    self.right_node.insert(key, data, False)

    def find_succesor_node(self, saved_nodes=None):
        if saved_nodes is None:
            saved_nodes = []

        if self.right_node is not None:
            saved_nodes.append(self.right_node)

        if self.left_node is None:
            return self, saved_nodes
        else:
            return self.left_node.find_succesor_node()

    def delete(self, key):
        if self.key is None:
            pass
        else:
            if key < self.key:
                if self.left_node is None:
                    pass

                elif self.left_node.key == key:
                    if (self.left_node.left_node is not None) or (self.left_node.right_node is not None):

                        if self.left_node.left_node is None:        # jedno dziecko
                            self.left_node = self.left_node.right_node
                        elif self.left_node.right_node is None:         #jedno dziecko v2
                            self.left_node = self.left_node.left_node
                        else:                                              #dwoje dzieci
                            succesor, saved_nodes = self.left_node.right_node.find_succesor_node()
                            if succesor != self.left_node.right_node:
                                self.delete(succesor.key)
                                self.left_node.key = succesor.key
                                self.left_node.data = succesor.data
                                for node in saved_nodes:
                                    self.left_node.right_node.insert(node)
                            else:
                                succesor.left_node = self.left_node.left_node
                                self.left_node = succesor
                    else:                                                   # zero dzieci
                            self.left_node = None
                else:
                    self.left_node.delete(key)

            elif key > self.key:
                if self.right_node is None:
                    pass

                elif self.right_node.key == key:
                    if (self.right_node.left_node is not None) or (self.right_node.right_node is not None):

                        if self.right_node.left_node is None:        # jedno dziecko
                            self.right_node = self.right_node.right_node
                        elif self.right_node.right_node is None:         #jedno dziecko v2
                            self.right_node = self.right_node.left_node
                        else:                                              #dwoje dzieci
                            succesor, saved_nodes = self.right_node.right_node.find_succesor_node()
                            if succesor != self.right_node.right_node:
                                self.delete(succesor.key)
                                self.right_node.key = succesor.key
                                self.right_node.data = succesor.data
                                for node in saved_nodes:
                                    self.right_node.right_node.insert(node)
                            else:
                                succesor.left_node = self.right_node.left_node
                                self.right_node = succesor
                    else:                                                   # zero dzieci
                            self.right_node = None
                else:
                    self.right_node.delete(key)

            elif key == self.key:           #usuwanie root
                if self is None:
                    pass
                elif (self.left_node is None) and (self.right_node is None):  # zero dzieci
                    self.key = None
                    self.data = None

                if (self.left_node is not None) or (self.right_node is not None):

                    if (self.right_node is None) or (self.left_node is None):  # jedno dziecko
                        if self.right_node:
                            self.key = self.right_node.key
                            self.data = self.right_node.data
                            if self.right_node.left_node:
                                self.right_node = self.right_node.left_node
                            elif self.right_node.right_node:
                                self.right_node = self.right_node.right_node
                            else:
                                self.right_node = None
                            self.root = self
                        elif self.left_node:
                            self.key = self.left_node.key
                            self.data = self.left_node.data
                            if self.left_node.left_node:
                                self.left_node = self.left_node.left_node
                            elif self.left_node.right_node:
                                self.left_node = self.left_node.right_node
                            else:
                                self.left_node = None
                            self.root = self

                    else:
                        succesor, saved_nodes = self.right_node.find_succesor_node()
                        self.delete(succesor.key)
                        self.data = succesor.data
                        self.key = succesor.key
                        for node in saved_nodes:
                            self.right_node.insert(node)
                        self.root = self

    def find_minimal(self):
        if self.left_node is None:
            return self
        else:
            return self.left_node.find_minimal()

    def find_maximal(self):
        dupa = self.key
        if self.right_node is None:
            return self
        else:
            return self.right_node.find_maximal()

    def print(self, lista_min=None, lista_max=None):
        import copy
        copy = copy.deepcopy(self)
        if lista_max is None:
            lista_max = []
        if lista_min is None:
            lista_min = []

        minimal = self.find_minimal()

        maximal = self.find_maximal()

        dupa1 = minimal.key
        dupa2 = maximal.key

        if minimal == maximal:
            string = ''
            lista_max.reverse()
            for node in lista_min:
                string += f'{node.key} {node.data}, '
            string += f'{self.root.key} {self.root.data}'
            for node in lista_max:
                string += f', {node.key} {node.data}'
            print(string)
        else:
            if minimal != self.root:
                copy.delete(minimal.key)
                lista_min.append(minimal)
            if maximal != self.root:
                lista_max.append(maximal)
                copy.delete(maximal.key)
            copy.print(lista_min, lista_max)

    def __one_branch_height(self, h: int = 0):
        if self.left_node:
            h += 1
            return self.left_node.__one_branch_height(h)
        elif self.right_node:
            h += 1
            return self.right_node.__one_branch_height(h)
        else:
            return h, self.key

    def height(self):
        import copy
        copy = copy.deepcopy(self)
        h = 0
        list_of_branches = []
        while h != 1:
            h, key = copy.__one_branch_height()
            copy.delete(key)
            list_of_branches.append(h)
        return max(list_of_branches)


    def print_tree(self):
        print("==============")
        self._print_tree(self.root, 0)
        print("==============")

    def _print_tree(self, node, lvl):
        if node is not None:
            self._print_tree(node.right_node, lvl + 5)

            print()
            print(lvl * " ", node.key, node.data)

            self._print_tree(node.left_node, lvl + 5)


keys = [50, 15, 62, 5, 20, 58, 91, 3, 8,  37, 60, 24]
data = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L']

tree = TreeNode(None, None)

for i in range(len(data)):
    tree.insert(keys[i], data[i])

tree.print_tree()

tree.print()

print(tree.search(24))
tree.insert(20, 'AA')

tree.insert(6, 'M')
tree.delete(62)
tree.insert(59, 'N')
tree.insert(100, 'P')
tree.delete(8)
tree.delete(15)
tree.insert(55, 'R')
tree.delete(50)
tree.delete(5)
tree.delete(24)
print(tree.height())
tree.print()
tree.print_tree()