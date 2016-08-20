import math

class Distance():
    """ Distance between two points. """

    def challengeInput(self):
        """ Input for this challenge. 
            Example input:
            1.0 7.0
            5.0 9.0
        """
        firstLine = input().split(' ')
        secondLine = input().split(' ')
        numbers = []
        for s in firstLine:
            numbers.append(float(s) )
        for s in secondLine:
            numbers.append(float(s) )
        return numbers

    def challengeOutput(self, numbers):
        """ Output for this challenge. 
            Example output from appropriate entry:
            1.0 7.0
            5.0 9.0
            4.4721
        """
        x1 = numbers[0]
        x2 = numbers[2]
        y1 = numbers[1]
        y2 = numbers[3]
        return math.sqrt(math.pow((x2 - x1), 2) + math.pow((y2 - y1), 2))

if __name__ == '__main__':
    dist = Distance()
    userInput = dist.challengeInput()
    print('%.4f' % dist.challengeOutput(userInput))

