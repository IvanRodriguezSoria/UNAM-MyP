import fileinput

class Painting():
    """
    Programming challenge number 1650.
    From https://www.urionlinejudge.com.br/judge/es/  
    """
    def challenge_in(self):
        """
        Returns a list with all the lines the user enters.
        """
        user_in = list()
        for line in fileinput.input():
            user_in.append(line)
        return user_in

    def challenge_out(self, user_in):
        """
        Output for this challenge.
        """
        for line in user_in:
            n, m, c = map(int, line.split(' ') )
            if n == 0 and m == 0 and c == 0:
                break
            print(self.get_all_boards(n - 7, m - 7, c) )

    def get_all_boards(self, n, m, c):
        """
        Returns n times m divided by 2. If c is 1, i add 1
        to the multiplication.
        """
        if n <= 0 or m <= 0:
            return 0
        if c == 1:
            return ((n * m) + 1) // 2
        return (n * m) // 2

if __name__ == '__main__':
    p = Painting()
    user_in = p.challenge_in()
    p.challenge_out(user_in)
