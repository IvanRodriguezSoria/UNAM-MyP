import fileinput

class BinaryLover():
    """
    Programming challenge number #TODO.
    From: 
    """
    def challenge_in(self):
        """
        Input for this challenge.
        For every case prints the result.
        """
        b_list = self.integer_to_binary()
        for line in fileinput.input():
            n = int(line)
            print(self.get_exact_division(n, b_list) )

    def get_exact_division(self, n, b_list):
        """
        For every decimal number in "b_list", returns the first
        number that can be divided exactly by n, if this number
        exist. If this number don't exist returns or is bigger
        than 10¹², returns -1.

        n       The number that divides the elements of "b_list".
        b_list  A list of all the permutations of 2 numbers (1 and 0).
                From 1 to 10¹²
        """
        for i in b_list:
            if i % n == 0:
                return i
        return -1

    def integer_to_binary(self):
        """
        Converts the decimal numbers from 1 to 496 to his binary
        representation. Then converts every binary number to a decimal
        one and returs a list containing this numbers.
        """
        b_list = list()
        for i in range(1, 4097):
            n_bin = bin(i)[2:]
            n_int = int(n_bin)
            b_list.append(n_int)
        return b_list

if __name__ == '__main__':
    bl = BinaryLover()
    bl.challenge_in()
