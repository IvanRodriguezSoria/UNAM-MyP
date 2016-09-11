import fileinput

class DuduServiceMaker():
    """
    Challenge number 1610 from
    https://www.urionlinejudge.com.br/judge/es/
    """
    class Graph():

        class Node():
        
            def __init__(self, value):
                self.value = value
                self.connections = set()

        def __init__(self, n):
            self.aux_dict = dict()
            self.node_set = set()
            for i in range(n):
                self.node_set.add(self.Node(i + 1) )

        def has_loop(self):
            for node in self.node_set:
                if self.__loop_aux(node, self.aux_dict):
                    return 'SIM'
                self.aux_dict = dict()
            return 'NAO'

        def __loop_aux(self, node, aux_dict):
            if node.value in self.aux_dict:
                return True
            if len(node.connections) < 1:
                return False
            self.aux_dict[node.value] = -1
            for n in node.connections:
                if self.__loop_aux(n, aux_dict):
                    return True
            return False

        def add_connection(self, a, b):
            node_a = self.find_node(a)
            node_b = self.find_node(b)
            node_a.connections.add(node_b)

        def find_node(self, node):
            for n in self.node_set:
                if n.value == node:
                    return n
            return None
    
    def challenge_in(self):
        user_in = list()
        for line in fileinput.input():
            user_in.append(line)
        return user_in

    def challenge_out(self, user_in):
        index = 0
        cases = int(user_in[index] )
        index += 1
        for i in range(cases):
            numbers = user_in[index].split()
            index += 1
            n = int(numbers[0])
            m = int(numbers[1])
            graph = self.Graph(n)
            for j in range(m):
                numbers = user_in[index].split()
                index += 1
                a = int(numbers[0])
                b = int(numbers[1])
                graph.add_connection(a, b)
            print(graph.has_loop() ) 

if __name__ == '__main__':
    dsm = DuduServiceMaker()
    user_in = dsm.challenge_in()
    dsm.challenge_out(user_in)
