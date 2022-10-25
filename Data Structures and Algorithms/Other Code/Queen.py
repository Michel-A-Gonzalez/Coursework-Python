
class Queens (object):

    def __init__ (self, n = 8):

        self.board = []

        self.n = n

        for i in range (0, self.n):

            row = []

            for j in range (0, self.n):

                row.append('*')

            self.board.append (row)

    def print_board (self):

        for i in range(0, self.n):

            for j in range(0 ,self.n):

                print (self.board[i][j], end = '')

            print()

        print()

    def is_valid (self, row, col):

        for i in range (0, self.n):

            if (self.board[row][i] == 'Q' or self.board[i][col] == 'Q'):

                return False

        for i in range (0, self.n):

            for j in range (0, self.n):

                row_diff = abs (row - i)

                col_diff = abs (col - j)

                if (row_diff == col_diff) and (self.board[i][j] == 'Q'):

                    return False

        return True

    def recursive_solve ( self, col):

        if (col == self.n):

            return True

        else:

            for i in range (0, self.n):

                if (self.is_valid (i, col)):

                    self.board[i][col] = 'Q'

                    if (self.recursive_solve (col + 1)):

                        return True

                    else:
                        
                        self.board[i][col] = '*'

            return False

    def solve (self, lst):

        for i in range (0, self.n):

            if (self.recursive_solve(i)):

                self.print_board()
            

def main ():

    game = Queens(4)

    game.solve([])

main()

            

                

        

    
