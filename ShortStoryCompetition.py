
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
        
        # TODO Don't work in all cases.
        lines = 0
        j = 0
        w = story.split()
        for i in range(number_of_words):
            j += len(w[i])
            if i == len(w) - 1:
                if j == max_chars:
                    continue
                else:
                    lines += 1
            else:
                j += 1
                if j == max_chars:
                    lines += 1
                    j = 0
                elif j > max_chars:
                    lines += 1
                    j = len(w[i]) + 1
        pages = math.ceil(lines / max_lines)
        return pages

if __name__ == '__main__':
    stc = ShortStoryCompetition()
    user_input = stc.challenge_input()
    stc.challenge_output(user_input)

