import fileinput

class Squares():
    
    def Sum(self):
        numbers = set()
        for i in range(10001):
            for j in range(10001):
                result = i**2 + j**2
                if result > 10000:
                    break
                numbers.add(result)
        return numbers

    def Out(self):
        numbers = self.Sum()
        for line in fileinput.input():
            number = int(line)
            if number in numbers:
                print('YES')
            else:
                print('NO')


if __name__ == '__main__':
    s = Squares()
    s.Out()