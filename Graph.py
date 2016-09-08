class Graph():
    """
    Graph class.
    """
    class Node():
        """
        Internal Node class.
        """
        def __init__(self, value):
            """
            Constructor.

            value   The value of this node (string).
            """
            # Sring value of this node.
            self.value = value
            # Mark of this node (Use this to walk the graph).
            self.mark = False
            # dictionary of connections to this node.
            self.connections = dict()

    def __init__(self, *args):
        """
        Construtor.

        value   Nodes of this graph(string).
        """
        self.nodes_dict = dict()
        for n in args:
            node = self.Node(n)
            self.add_node(node)

    def new_node(self, value, *args):
        """
        Creates a new node.

        value   The value of this node (string).
        args    The connections with this node (strings).
        """
        node = self.Node(value)
        self.add_connections(node, args)
        return node

    def add_node(self, node, *args):
        """
        Adds a new node to the graph.

        node    Node to be added to the graph.
        args    Connections with this node.
        """
        if node.value not in self.nodes_dict:
            self.nodes_dict[node.value] = node
        self.add_connections(node, args)

    def find_node(self, value):
        """
        Finds a node with a given value.
        Returns the node in the graph or None otherwise.

        value   The value of the node to find (string).
        """
        if value in self.nodes_dict:
            return self.nodes_dict[value]
        return None

    def add_connections(self, node, *args):
        """
        Adds new connections to the given node.
        
        node    The node to add connections.
        args    The connections with the node (string).
        """
        for e in args:
            n = self.find_node(e)
            if n is None:
                node.connections[e] = self.Node(e)
            else:
                node.connections[e] = n

    def has_loops(self):
        """
        Return True if the graph has loops and
        False otherwise.
        """
        for k, v in self.nodes_dict.items():
            v.mark = True
            for k1, v1 in v.connections.items():
                if v1.mark == True:
                    return True
                v1.mark = True
            self.__erase_marks()
        return False

    def __erase_marks(self):
        """
        Erase all marks of the nodes dict.
        """
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
