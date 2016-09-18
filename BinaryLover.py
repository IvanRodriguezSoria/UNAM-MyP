import fileinput

class BinaryLover():

    #TODO This takes too much time. Need to workout the solution.
    def challenge_in(self):
        for line in fileinput.input():
            n = int(line)
            for i in range(2, 1000000000000):    
                m_str = str(n * i)
                if self.check_01(m_str):
                    print(m_str)
                    break
                if len(m_str) > 1000000000000:
                    print(-1)
                    break

    def check_01(self, n):
        for char in n:
            if char == '1' or char == '0':
                continue
            else:
                return False
        return True

    def challenge_out(self, user_in):
        pass

if __name__ == '__main__':
    bl = BinaryLover()
    bl.challenge_in()
