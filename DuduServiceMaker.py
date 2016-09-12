import fileinput

class DuduServiceMaker():
    """
    Challenge number 1610 from
    https://www.urionlinejudge.com.br/judge/es/
    """
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
            graph = [None for x in range(n + 1)]
            has_loops = False
            for j in range(m):
                numbers = user_in[index].split()
                index += 1
                a = int(numbers[0])
                b = int(numbers[1])
                graph[a] = b
            for k in range(1, n + 1):
                has_loops = self.__aux(graph, k, dict() )
                if has_loops:
                    break
            if has_loops:
                print('SIM')
            else:
                print('NAO')

    def __aux(self, graph, index, aux_dict):
        index = graph[index]
        if index == None:
            return False
        if index in aux_dict:
            return True
        aux_dict[index] = 0
        return self.__aux(graph, index, aux_dict)

if __name__ == '__main__':
    dsm = DuduServiceMaker()
    user_in = dsm.challenge_in()
    dsm.challenge_out(user_in)
