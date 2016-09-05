
import fileinput

class PlayingWithOperators():

    def challenge_input(self):
        user_input = list()
        for line in fileinput.input():
            user_input.append([int(i) for i in line.split()])
        return user_input

    def challenge_output(self, user_input):
        cases = user_input[0][0]
        index = 1
        add = True
        flag = True
        for i in range(cases):
            first_line = user_input[index]
            index += 1
            game_elements = user_input[index]
            index += 1
            replacements = first_line[1]
            n = self.__start_game(game_elements, add)
            print(self.__get_winner(n, flag) )
            for j in range(replacements):
                numbers_to_switch = user_input[index]
                index += 1
                a = numbers_to_switch[0]
                b = numbers_to_switch[1]
                game_elements[a - 1] = b
                n = self.__start_game(game_elements, add)
                print(self.__get_winner(n, flag) )
            flag = not flag

    def __start_game(self, game_elements, add):
        return self.__get_n(game_elements, add)

    def __get_n(self, game_elements, add):
        n_list = list()
        length = len(game_elements)
        is_odd = False
        if length <= 1:
            return game_elements[0]
        if length % 2 != 0:
            is_odd = True
            length -= 1
        for i in range(0, length, 2):
            n_list.append(self.__switch_operator(game_elements[i], game_elements[i + 1], add) )
        if is_odd:
            n_list.append(game_elements[-1])
        return self.__get_n(n_list, not add)

    def __switch_operator(self, n, m, add):
        if add:
            return n + m
        return n - m

    def __get_winner(self, number, flag):
        if flag:
            winner = 'Rusa'
            if number % 2 == 0:
                winner = 'Sanches'
            return '{} {}'.format(number, winner)
        winner = 'Sanches'
        if number % 2 == 0:
            winner = 'Rusa'
        return '{} {}'.format(number, winner)

if __name__ == '__main__':
    pwo = PlayingWithOperators()
    user_input = pwo.challenge_input()
    pwo.challenge_output(user_input)
