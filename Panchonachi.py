
import time

class Panchonachi():
    """ Represents the 3 different Panchonachi algoriths i know.
        Panchonachi is a Fibonacci-like number sequence
        Each method returns the Panchonachi number in the n position
        but with different complexity.
        Example: The 3 Panchonachi number will be 5.
    """

    def __init__(self):
        pass

    def exponential(self, n):
        """ Time complexity: O(n^2).

            n   The position of the Panchonachi number.
        """
        if n in [1,2,3]: 
            return {1:2, 2:3, 3:5}[n] 
        else: 
            return 13*self.exponential(n-1)+ 11*self.exponential(n-2) + 7*self.exponential(n-3)

    def linear(self, n):
        """ Time complexity: O(n).

            n   The position of the Panchonachi number.
        """
        p1, p2, p3 = 2, 3, 5 
        for index in range(n-1): 
            p1, p2, p3 = p2, p3, 7*p1 + 11*p2 + 13*p3 
        return p1

    def logarithmic(self, n):
        """ Time complexity: O(longn).

            n   The position of the Panchonachi number.
        """
        a = [5, 3, 2]
        b = [13, 11, 7, 1, 0, 0, 0, 1, 0]

        if n == 1:
            return a[2]
        elif n == 2:
            return a[1]
        elif n == 3:
            return a[0]

        b = self.__power(n - 3, b)
        a = self.__matrixMultiplication3x2(a, b)
        return a[0]

    def __matrixMultiplication3x2(self, a, b):
        """ Multiplies two different matrix, and returns the result.

            a   The first 1x3 matrix.
            b   The second 3x3 matrix.
        """
        return [(b[0]*a[0]) + (b[1]*a[1]) + (b[2]*a[2]),
                (b[3]*a[0]) + (b[4]*a[1]) + (b[5]*a[2]),
                (b[6]*a[0]) + (b[7]*a[1]) + (b[8]*a[2])]

    def __matrixMultiplication3x3(self, a, b):
        """ Multiplies two 3x3 matrix, and returns the result.

            a   The first 3x3 matrix.
            b   The second 3x3 matrix.
        """
        return [(b[0]*a[0]) + (b[1]*a[3]) + (b[2]*a[6]), (b[0]*a[1]) + (b[1]*a[4]) + (b[2]*a[7]),
                (b[0]*a[2]) + (b[1]*a[5]) + (b[2]*a[8]), 
                (b[3]*a[0]) + (b[4]*a[3]) + (b[5]*a[6]), (b[3]*a[1]) + (b[4]*a[4]) + (b[5]*a[7]),
                (b[3]*a[2]) + (b[4]*a[5]) + (b[5]*a[8]),
                (b[6]*a[0]) + (b[7]*a[3]) + (b[8]*a[6]), (b[6]*a[1]) + (b[7]*a[4]) + (b[8]*a[7]),
                (b[6]*a[2]) + (b[7]*a[5]) + (b[8]*a[8])]

    def __power(self, n, b):
        """ Returns the power n of a 3x3 special matrix.
            Special matrix: | 13 | 11 | 7  |
                            | 1  | 0  | 0  |
                            | 0  | 1  | 0  |

            n   The desired power of the matrix.
        """
        if n == 1:
            return b
        if n % 2 == 0:
            rec = self.__power(n // 2, b)
            return self.__matrixMultiplication3x3(rec, rec)
        else:
            rec = self.__power((n - 1) // 2, b)
            return self.__matrixMultiplication3x3(self.__matrixMultiplication3x3(rec, rec), b)  

if __name__ == '__main__':

    print('\nPanchonachi class test.')

    pancho = Panchonachi()
    
    start = time.time()
    print('\n\nO(n^2) The 15 Panchonachi number:')
    print(pancho.exponential(15) )
    end = time.time()
    print(end - start)
    
    start = time.time()
    print('\n\nO(n) The 15 Panchonachi number:')
    print(pancho.linear(15) )
    end = time.time()
    print(end - start)

    start = time.time()
    print('\n\nO(logn) The 15 Panchonachi number:')
    print(pancho.logarithmic(15) )
    end = time.time()
    print(end - start)
    
