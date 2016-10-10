import fileinput

class TurnLeft () :
    """
    Uri challenge number 1437.
    From: https://www.urionlinejudge.com.br
    """

    def challenge_in (self) :
        """
        Input for this challenge.
        """
        user_in = list()
        for i in fileinput.input() :
            user_in.append(i.strip() )
        return user_in

    def challenge_out (self, user_in) :
        """
        Output for this challenge.

        user_in     List containing all the lines the user enter.
        """
        wind_rose = ['N', 'L', 'S', 'O']
        index = 1
        lenght = len(user_in)
        while index < lenght :
            commands = user_in[index]
            final_orientation = self.orientation(commands)
            print(wind_rose[final_orientation])
            index += 2


    def orientation (self, commands) :
        """
        Given a list of commands, returns an int, indicating the final 
        orientation of a recruit. That is, if the int is 3, the final 
        orientation is West (Avaible options are: [North, East, South, West]
        [0, 1, 2, 3]).

        commands    List of commands E and D. 
        """
        final_orientation = 0
        for command in commands :
            if command == 'E' :
                if final_orientation == 0 :
                    final_orientation = 3
                else :
                    final_orientation -= 1
            else :
                if final_orientation == 3 :
                    final_orientation = 0
                else :
                    final_orientation += 1
        return final_orientation

if __name__ == '__main__' :
    tl = TurnLeft()
    user_in = tl.challenge_in()
    tl.challenge_out(user_in)