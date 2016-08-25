
import fileinput
import math

class ShortStoryCompetition():
    """ Uri Online Judge challenge number 1222 """

    def challenge_input(self):
        """ Input example:
            5 2 2
            a e i o u
        """
        user_input = list()
        for line in fileinput.input():
            user_input.append(line)
        return user_input

    def challenge_output(self, user_input):
        """ Output example:
            3

            user_input  An array with the "limit numbers" and the "short stories"
        """
        for i in range(0, len(user_input), 2):
            numbers = user_input[i]
            story = user_input[i + 1]
            print(self.__number_of_pages(numbers, story) )

    def __number_of_pages(self, numbers, story):
        """ Returns the number of pages the story will need,
            given the appropiate data 
            
            numbers limit numbers
            story   short story
        """
        numbers_list = numbers.split()
        number_of_words = int(numbers_list[0])
        max_lines = int(numbers_list[1])
        max_chars = int(numbers_list[2])
        
        lines = 0
        char_counter = 0
        words = story.split()
        for i in range(number_of_words):
            if i == 0:
                char_counter = len(words[i])
                lines += 1
            else:
                char_counter += 1 + len(words[i])
                if char_counter > max_chars:
                    char_counter = len(words[i])
                    lines += 1
        pages = math.ceil(lines / max_lines)
        return pages

if __name__ == '__main__':
    stc = ShortStoryCompetition()
    user_input = stc.challenge_input()
    stc.challenge_output(user_input)

