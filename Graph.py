class Graph():

    class Node():

        def __init__(self, value):
            self.value = value
            self.mark = False
            self.connections = dict()

    def __init__(self, *args):
        self.nodes_dict = dict()
        for n in args:
            node = self.Node(n)
            self.add_node(node)

    def new_node(self, value, *args):
        node = self.Node(value)
        self.add_connections(node, args)
        return node

    def add_node(self, node, *args):
        if node.value not in self.nodes_dict:
            self.nodes_dict[node.value] = node
        self.add_connections(node, args)

    def find_node(self, value):
        if value in self.nodes_dict:
            return self.nodes_dict[value]
        return None

    def add_connections(self, node, *args):
        for e in args:
            n = self.find_node(e)
            if n is None:
                node.connections[e] = self.Node(e)
            else:
                node.connections[e] = n

    def has_loops(self):
        for k, v in self.nodes_dict.items():
            v.mark = True
            for k1, v1 in v.connections.items():
                if v1.mark == True:
                    return True
                v1.mark = True
            self.__erase_marks()
        return False

    def __erase_marks(self):
        for k, v in self.nodes_dict.items():
            v.mark = False

if __name__ == '__main__':
    g = Graph(1, 2, 3, 4, 5)
    n5 = g.find_node(5)
    g.add_connections(n5, '4')
    print(g.has_loops() )
    n4 = g.find_node(4)
    g.add_connections(n4, '5')
    print(g.has_loops() )
