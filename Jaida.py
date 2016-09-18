import fileinput

class Jaida():
    """
    Programming challenge number 1697.
    From https://www.urionlinejudge.com.br/judge/es/ 
    """

    def challenge_in(self):
        """
        Input for this challenge.
        Returns a list with all the lines the user enter.
        """
        user_in = list()
        for line in fileinput.input():
            user_in.append(line)
        return user_in

    def challenge_out(self, user_in):
        """
        Output for this challenge.

        user_in     A list with all the lines the user enter.
        """
        sieve = self.sieve_eratosthenes()
        index = 0
        cases = int(user_in[0])
        index += 2
        for i in range(cases):
            numbers_dict = dict()
            for n in user_in[index].split():
                numbers_dict[int(n)] = 0
            print(self.check_max(numbers_dict, sieve) )
            index += 2

    def sieve_eratosthenes(self):
        """
        Classic Eratosthenes algorithm.
        Returns a list with all the prime numbers
        from 1 to 2000000.
        """
        size = 2000000
        sieve = [True] * size
        sieve_list = [1]
        index = 0
        for i in range(2, size):
            if sieve[i] == False:
                continue
            sieve_list.append(i)
            for j in range(2, size):
                index = i * j
                if index > size - 1:
                    break
                sieve[index] = False
        return sieve_list

    def check_max(self, numbers_dict, sieve):
        """
        For every prime number in "sieve", checks if
        the prime number is in "numbers_dic".
        If the prime number is not in "numbers_dict"
        returns the prime number minus 1, else returns -1.

        numbers_dict    A dictionary with the numbers to check (The key).
        sieve           A list with all the prime numbers in a range (1, 2000000).
        """
        for i in sieve:
            if i not in numbers_dict:
                return i - 1
        return -1

if __name__ == '__main__':
    j = Jaida()
    user_in = j.challenge_in()
    j.challenge_out(user_in)
