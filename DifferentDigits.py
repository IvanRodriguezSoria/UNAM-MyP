
import fileinput

class DifferentDigits():
    """ Given two integers N and M, determines the maximum number
        of numbers between N and M, inclusive, that do not have repeated digits.
    """
    def challengeOutput(self):
        """ Challenge input. Example with the appropriate entry:
            87 104
            14
        """
        n, m = 0, 0
        for line in fileinput.input():
            uniqueNumbers = 0
            n, m = map(int, line.split(' '))
            for i in range(n, m + 1):
                if self.__hasUniqueDigits(i):
                    uniqueNumbers += 1
            print(uniqueNumbers)

    def __hasUniqueDigits(self, n):
        """ If an integer has repeated digits returns True.
            else returns False.
            Example: 112 returns True.

            n   The number to check for repeated digits.
        """
        aux = str(n)
        data = set()
        for number in aux:
            data.add(number)
        return len(data) == len(aux)

if __name__ == '__main__':
    dg = DifferentDigits()
    dg.challengeOutput()

