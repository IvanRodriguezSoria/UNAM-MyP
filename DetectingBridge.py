import fileinput

class DetectingBridges():
    """
    Challenge number 1790 from
    https://www.urionlinejudge.com.br/judge/es/
    """
    def __init__(self):
        self.result = 0

    def challenge_in(self):
        user_in = list()
        for line in fileinput.input():
            user_in.append(line)
        return user_in

    def challenge_out(self, user_in):
        index = 0
        cities_and_bridges = user_in[index].split()
        index += 1
        cities = int(cities_and_bridges[0])
        bridges = int(cities_and_bridges[1])
        graph = [None for x in range(cities + 1)]
        ####################################
        for i in range(bridges):
            x_and_y = user_in[index].split()
            index += 1
            x = int(x_and_y[0])
            y = int(x_and_y[1])
            graph[x] = y
        # TODO Needs Tarjan algorith.

if __name__ == '__main__':
    db = DetectingBridges()
    user_in = db.challenge_in()
    db.challenge_out(user_in)
