
import time

class Fibonacci():
    """ Represents the 3 different Fibonacci algoriths i know. 
        Each method returns the Fibonacci number in the n position
        but with different complexity.
        Example: The 6 Fibonacci number will be 8.
    """

    def __init__(self):
        self.a = [1, 1, 1, 0]
        self.b = [1, 1, 1, 0]

    def exponential(self, n):
        """ Time complexity: O(n^2).

            n   The position of the Fibonacci number.
        """
        if n == 0 or n == 1:
            return n
        else:
            return self.exponential(n - 1) + self.exponential(n - 2)
        
    def linear(self, n):
        """ Time complexity: O(n).

            n   The position of the Fibonacci number.
        """
        if n == 0 or n == 1:
            return n

        last, current = 0, 1
        for i in range(1, n):
            last, current = current, current + last
        return current

    def logarithmic(self, n):
        """ Time complexity: O(longn).

            n   The position of the Fibonacci number.
        """
        if n == 0 or n == 1:
            return n

        self.__power(n)
        return self.b[2]
        """
        return self.b[1]
        """

    def __matrixMultiplication(self, a, b):
        """ Multiplies two 2x2 matrix, and returns the result.

            a   The first 2x2 matrix.
            b   The second 2x2 matrix.
        """
        return [(b[0] * a[0]) + (b[1] * a[2]), (b[0] * a[1]) + (b[1] * a[3]), 
                (b[2] * a[0]) + (b[3] * a[2]), (b[2] * a[1]) + (b[3] * a[3])]

    def __power(self, n):
        """ Returns the power n of a 2x2 special matrix.
            Special matrix: | 1 | 1 |
                            | 1 | 0 |

            n   The desired power of the matrix.
        """
        if n == 1:
            return
        self.__power(n // 2)
        self.b = self.__matrixMultiplication(self.b, self.b)
        if n % 2 != 0:
            self.b = self.__matrixMultiplication(self.a, self.b)

if __name__ == '__main__':

    print('\nFibonacci class test.')

    fibo = Fibonacci()
    
    start = time.time()
    print('\n\nO(n^2) The 30 Fibonacci number:')
    print(fibo.exponential(30) )
    end = time.time()
    print(end - start)
    
    start = time.time()
    print('\n\nO(n) The 30 Fibonacci number:')
    print(fibo.linear(30) )
    end = time.time()
    print(end - start)

    start = time.time()
    print('\n\nO(logn) The 30 Fibonacci number:')
    print(fibo.logarithmic(30) )
    end = time.time()
    print(end - start)
    
