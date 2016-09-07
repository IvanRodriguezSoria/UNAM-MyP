import fileinput
import math

class Shuffling():
    """
    Challenge number 1980 from
    https://www.urionlinejudge.com.br/judge/es/
    """
    def challenge_in(self):
        """
        Challenge input.
        """
        user_in = list()
        for line in fileinput.input():
            user_in.append(line.strip(' \t\n\r') )
        return user_in

    def challenge_out(self, user_in):
        """
        Challenge output.

        user_in     User input.
        """
        for s in user_in:
            length = len(s)
            if length == 0 or s == '0':
                return
            print(math.factorial(length) )

if __name__ == '__main__':
    sh = Shuffling()
    user_in = sh.challenge_in()
    sh.challenge_out(user_in)
