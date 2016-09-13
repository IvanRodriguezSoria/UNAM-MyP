import fileinput

class DuduServiceMaker():
    """
    Challenge number 1610 from
    https://www.urionlinejudge.com.br/judge/es/
    """
    class Graph():

        def __init__(self, n):
            self.node_dict = dict()
            for i in range(1, n + 1):
                self.node_dict[i] = set()

        def add_connection(self, a, b):
            self.node_dict[a].add(b)

        def cyclic(self, g):
            path = set()
            visited = set()

            def visit(vertex):
                if vertex in visited:
                    return False
                visited.add(vertex)
                path.add(vertex)
                for neighbour in g.get(vertex, ()):
                    if neighbour in path or visit(neighbour):
                        return True
                path.remove(vertex)
                return False

            return any(visit(v) for v in g)

        # TODO Not Working for the pice of shit Uri online judge
        # and i don't know why.
        def DFS_has_loops(self, start):
            visited = set()
            stack = [start]
            while stack:
                vertex = stack.pop()
                if vertex not in visited:
                    visited.add(vertex)
                    stack.extend(self.node_dict[vertex])
                else:
                    return True
            return False

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
            d = dict()
            for j in range(m):
                numbers = user_in[index].split()
                index += 1
                a = int(numbers[0])
                b = int(numbers[1])
                graph.add_connection(a, b)
            if graph.cyclic(graph.node_dict):
                print('SIM')
            else:
                print('NAO')

if __name__ == '__main__':
    dsm = DuduServiceMaker()
    user_in = dsm.challenge_in()
    dsm.challenge_out(user_in)
