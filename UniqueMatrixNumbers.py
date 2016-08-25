
import time

class UniqueMatrixNumbers():
    """ Using different data structures (Actually this class
        only use 2), i implement an algorith to find how many
        not repeated numers a matrix have.
    """

    def uniqueNumbersDict(self, n, m):
        """ Using a dictionary as the primary data structure
            this method finds how many not repeated numers
            a (n * m) matrix have.

            n   The rows to be multiplied to make a matrix.
            m   The columns to be multiplied to make a matrix.
        """
        numbers = dict()
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                numbers[i ** j] = 1
        return len(numbers.keys())

    def uniqueNumbersSet(self, n, m):
        """ Using a set as the primary data structure
            this method finds how many not repeated numers
            a (n * m) matrix have.

            n   The rows to be multiplied to make a matrix.
            m   The columns to be multiplied to make a matrix.
        """
        numbers = set()
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                numbers.add(i ** j)
        return len(numbers)

    def uniqueNumbersSmall(self, n, m):
        """ Using a set as the primary data structure this 
            method finds how many not repeated numers a (n * m)
            matrix have.

            n   The rows to be multiplied to make a matrix.
            m   The columns to be multiplied to make a matrix.
        """
        return len(set(i ** j for i in range(1, n + 1) for j in range(1, m + 1)))

if __name__ == '__main__':

    n = UniqueMatrixNumbers()

    start = time.time()
    print(n.uniqueNumbersDict(100, 500))
    end = time.time()
    print(end - start)

    start = time.time()
    print(n.uniqueNumbersSet(100, 500))
    end = time.time()
    print(end - start)

    start = time.time()
    print(n.uniqueNumbersSmall(100, 500))
    end = time.time()
    print(end - start)

