class KnightsTour:

    def __init__(self, board_size):
        self.board_size = board_size
        self.h_moves = [2, 1, -1, -2, -2, -1, 1, 2]
        self.v_moves = [1, 2, 2, 1, -1, -2, -2, -1]
        self.solution_matrix = [[-1 for _ in range(self.board_size)] for _ in range(self.board_size)]

    def solve_problem(self):

    #start with top left cell
        self.solution_matrix[0][0] = 0

       #first paremeter is the counter next one will 2, 3,
       # the second and third parameter is the location (0, 0)
        if self.solve(1, 0, 0):
            self.print_solution()
        else:
            print('There is no solution...')

    def solve(self, piece_mvmt, h, v): # call solve function #row is h and column is v

        #base
        if piece_mvmt == self.board_size * self.board_size:
            return True

       #consider all possible moves
        for move_index in range(len(self.h_moves)): #for range in number of moves

            next_h = h + self.h_moves[move_index]
            next_v = v + self.v_moves[move_index]

            if self.is_valid_move(next_h, next_v): #if step is valid 
                
                self.solution_matrix[next_h][next_v] = piece_mvmt #update movement tracker

                if self.solve(piece_mvmt+1, next_h, next_v):
                    return True

                #backtrack if false
                #reinitialize solution with-1
             
                self.solution_matrix[next_h][next_v] = -1

        return False

    def is_valid_move(self, h, v): #making sure that the knight does not step outside the chessboard

      
        if h < 0 or h >= self.board_size: #does not step out horizontally
            return False

        
        if v < 0 or v >= self.board_size:#nor vertically
            return False

       
        if self.solution_matrix[h][v] > -1: #may have already checked cell and now number is not -1
            return False

        return True

    def print_solution(self):
        for i in range(self.board_size):
            for j in range(self.board_size):
                print(self.solution_matrix[i][j], end=' ')
            print('\n')


if __name__ == '__main__':

  
    tour = KnightsTour(8)
    tour.solve_problem()
