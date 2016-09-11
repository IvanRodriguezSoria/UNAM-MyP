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
            self.node_list = list()
            self.message = 0
            for i in range(n):
                self.node_list.append(self.Node(i + 1) )

        def has_loop(self):
            for node in self.node_list:
                self.__loop_aux(node)
                if self.message > 0:
                    break
                self.aux_dict = dict()
            if self.message > 0:
                return 'SIM'
            return 'NAO'

        def __loop_aux(self, node):
            if node.value in self.aux_dict:
                self.message += 1
                return
            if self.message > 0:
                return
            self.aux_dict[node.value] = -1
            for n in node.connections:
                self.__loop_aux(n)

        def add_connection(self, a, b):
            node_a = self.find_node(a)
            node_b = self.find_node(b)
            node_a.connections.add(node_b)

        def find_node(self, n):
            return self.node_list[n - 1]
    
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
