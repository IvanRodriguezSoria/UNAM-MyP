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
                self.mark = False
                self.connections = set()

            def has_loops(self, node):
                if node.mark:
                    return 'SIM'
                elif len(node.connections) < 1:
                    return 'NAO'
                node.mark = True
                message = ''
                for n in node.connections:
                    message = self.has_loops(n)
                return message

        def __init__(self, n):
            self.node_set = set()
            for i in range(n):
                self.node_set.add(self.Node(i + 1) )

        def add_connection(self, a, b):
            node_a = self.find_node(a)
            node_b = self.find_node(b)
            node_a.connections.add(node_b)

        def find_node(self, node):
            for n in self.node_set:
                if n.value == node:
                    return n
            return None

        def remove_marks(self):
            for node in self.node_set:
                node.mark = False
    
    def challenge_in(self):
        user_in = list()
        for line in fileinput.input():
            user_in.append(line.strip(' \r\n\t') )
        return user_in

    def challenge_out(self, user_in):
        index = 0
        cases = int(user_in[index] )
        index += 1
        for i in range(cases):
            message = 'NAO'
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
            for k in graph.node_set:
                message = k.has_loops(k)
                graph.remove_marks()
            print(message) 

if __name__ == '__main__':
    dsm = DuduServiceMaker()
    user_in = dsm.challenge_in()
    dsm.challenge_out(user_in)
