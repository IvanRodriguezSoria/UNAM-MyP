
import fileinput

class ArrayHash():
    """ Makes a hash code from a given input """

    def challenge_input(self):
        """ Example:
            1
            1
            ZZZZZZZZZZ
        """
        user_input = list()
        for line in fileinput.input():
            user_input.append(line[:-1])
        return user_input

    def challenge_output(self, user_input):
        """ Example with correct input:
            295

            user_input  The user input
        """
        test_cases = int(user_input[0])
        next_line = int(user_input[1])
        current_line = 2
        for i in range(test_cases):
            print(self.__get_hash(user_input[current_line : current_line + next_line], next_line) )
            if i != test_cases - 1:
                current_line += next_line + 1
                next_line = int(user_input[current_line - 1])
        
    def __get_hash(self, user_input, number_of_lines):
        """ Get hash codes from a given user input with a given number of lines.

            user_input      The user input (Upper case letter: ABCD)
            number_of_lines The number of lines in the user input.
        """
        hash_number = 0
        for i in range(number_of_lines):
            counter = 0
            for char in user_input[i]:
                hash_number += int(ord(char)) - 65 + counter + i
                counter += 1
        return hash_number

if __name__ == '__main__':
    ah = ArrayHash()
    user_input = ah.challenge_input()
    ah.challenge_output(user_input)
