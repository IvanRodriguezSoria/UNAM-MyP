import fileinput

class DetectingBridges():
    """
    Challenge number 1790 from
    https://www.urionlinejudge.com.br/judge/es/
    """
    class Graph():

        class Node():

            def __init__(self, value):
                self.value = value
                self.connections = list()

        def __init__(self, n):
            self.node_list = list()
            self.aux_dict = dict()
            self.message = 0
            for i in range(n):
                self.node_list.append(self.Node(i + 1) )

        def has_loop(self):
            for node in self.node_list:
                self.__loop_aux(node)
                self.aux_dict = dict()

        def __loop_aux(self, node):
            if node.value in self.aux_dict:
                self.message += 1
                return
            self.aux_dict[node.value] = 0
            for n in node.connections:
                self.__loop_aux(n)

        def add_connection(self, a, b):
            node_a = self.find_node(a)
            node_b = self.find_node(b)
            node_a.connections.append(node_b)

        def find_node(self, n):
            return self.node_list[n - 1]

    def challenge_in(self):
        user_in = list()
        for line in fileinput.input():
            user_in.append(line)
        return user_in

    def challenge_out(self, user_in):
        index = 0
        cities_and_bridges = user_in[index].split()
        cities = int(cities_and_bridges[0])
        bridges = int(cities_and_bridges[1])
        index += 1
        graph = self.Graph(cities)
        for i in range(bridges):
            x_and_y = user_in[index].split()
            index += 1
            x = int(x_and_y[0])
            y = int(x_and_y[1])
            graph.add_connection(x, y)
        graph.has_loop()
        print(bridges - graph.message)

if __name__ == '__main__':
    db = DetectingBridges()
    user_in = db.challenge_in()
    db.challenge_out(user_in)
