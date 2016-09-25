import fileinput

class HelpKiko():
    """
    Programming challenge number 1909
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
        Prints the desired output.

        user_in     List containing all the lines the user enter.
        """
        index = 0
        while index < len(user_in):
            n = int(user_in[index].strip(' \t\r\n').split(' ')[1])
            if n == 0:
                break
            index += 1
            numbers_list = list()
            numbers_dict = dict()
            strip_line = user_in[index].strip(' \t\r\n')
            index += 1
            for x in strip_line.split():
                number = int(x)
                numbers_list.append(number)
                numbers_dict[number] = 0
            b = self.result(numbers_list, n, numbers_dict)
            if b == -1:
                print('impossivel')
            else:
                print(b)

    def euclidean_algorithm(self, a, b):
        """
        Classic Euclidean algorithm. Gets the mcd of two values.
        "a" needs to be bigger or equal to "b".

        a   The first int value.
        b   The second int value.
        """
        a_max = max(a, b)
        b_min = min(a, b)
        if b_min == 0:
            return a_max
        return self.euclidean_algorithm(b_min, a_max % b_min)

    def get_b(self, a, n, numbers_dict):
        """
        Returns a "b" int.
        This "b" int is an unknow number such that mcm(a, b)
        is equal to an int "n".

        a               int know number.
        n               int equal to mcm(a, b). "b" is unknow.
        numbers_dict    dict containing int numbers such that
                        "b" can't be any number in the dict.'
        """
        for i in range(2, n + 1):
            if i in numbers_dict:
                continue
            mcd = self.euclidean_algorithm(a, i)
            if mcd == -1:
                continue
            if (a * i) / mcd == n:
                return i
        return -1

    def mcm(self, a, b):
        """
        Returns an int equal to mcm(a, b).

        a   First int number.
        b   Second int number.
        """
        return (a * b) / self.euclidean_algorithm(a, b)

    def result(self, numbers_list, n, numbers_dict):
        """
        Returns an int "b" such that mcm(a, b) = n.
        Or -1 if that "b" don't exist.
        
        numbers_list    int list with all the numbers to
                        calculate the mcm.
        n               int such that mcm(a, b) = n.
        numbers_dict    int key, value dict with all the
                        numbers to calculate the mcm.
        """
        for i in numbers_list:
            if n % i != 0:
                return -1
        index = 0
        a = numbers_list[index]
        index += 1
        while index < len(numbers_list):
            b = numbers_list[index]
            index += 1
            a = self.mcm(a, b)
        return self.get_b(a, n, numbers_dict)

if __name__ == '__main__':
    hk = HelpKiko()
    user_in = hk.challenge_in()
    hk.challenge_out(user_in)
