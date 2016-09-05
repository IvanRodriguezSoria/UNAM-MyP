
import fileinput

class PlayingWithOperators():

    def challenge_input(self):
        user_input = list()
        for line in fileinput.input():
            user_input.append(line)
        return user_input

    def challenge_output(self, user_input):
        cases = int(user_input[0])
        index = 1
        for i in range(cases):
            first_line = user_input[index].split()
            index += 1
            game_elements = [int(x) for x in user_input[index].split()] 
            index += 1
            replacements = int(first_line[1])
            print(self.__start_game(game_elements) )
            for j in range(replacements):
                numbers_to_switch = [int(x) for x in user_input[index].split()]
                index += 1
                a = numbers_to_switch[0]
                b = numbers_to_switch[1]
                game_elements[a - 1] = b
                print(self.__start_game(game_elements) )

    def __start_game(self, game_elements):
        return game_elements
        """length = len(game_elements)
        if length == 1:
            winner = 'Rusa'
            if game_elements[0] % 2 == 0:
                winner = 'Sanches'
            return '{} {}'.format(game_elements[0], winner)
        
        if length % 2 != 0:
            length -= 1
        
        new_game_elements = list()
        for i in range(0, length, 2):
            result = game_elements[i] + game_elements[i + 1]
            new_game_elements.append()"""

if __name__ == '__main__':
    pwo = PlayingWithOperators()
    user_input = pwo.challenge_input()
    pwo.challenge_output(user_input)
