from Solver import solveable, valid_moves
import unittest

class TestValidMoves(unittest.TestCase):
        def testValidMoves(self):
                """Tests that valid_moves returns correct positions"""
                # 'k' denotes a knight
                # 'x' denotes possible moves
                # Positions should be given in (row, column) tuples
                #  0 1 2 3 4 5 6 7
                #0 - - - - - - - -
                #1 - - - - - - - -
                #2 - - - - - - - -
                #3 - - - - - - - -
                #4 - - - - - - - -
                #5 - x - - - - - -
                #6 - - x - - - - -
                #7 k - - - - - - -
                # TODO: Fill in the data to test valid_moves on the board above
                k_idx = (0,7)
                expected_valid_moves = {(1,5), (2,6)}
                self.assertEqual(valid_moves(k_idx), expected_valid_moves)

                # TODO: Write tests for valid_moves for the following boards
                #  0 1 2 3 4 5 6 7
                #0 k - - - - - - -
                #1 - - x - - - - -
                #2 - x - - - - - -
                #3 - - - - - - - -
                #4 - - - - - - - -
                #5 - - - - - - - -
                #6 - - - - - - - -
                #7 - - - - - - - -
                k_idx = (0, 0)
                expected_valid_moves = {(1,2), (2,1)}
                self.assertEqual(valid_moves(k_idx), expected_valid_moves)

                #  0 1 2 3 4 5 6 7
                #0 - - - - - - - k
                #1 - - - - - x - -
                #2 - - - - - - x -
                #3 - - - - - - - -
                #4 - - - - - - - -
                #5 - - - - - - - -
                #6 - - - - - - - -
                #7 - - - - - - - -
                
                k_idx = (7,0)
                expected_valid_moves = {(5,1), (6,2)}
                self.assertEqual(valid_moves(k_idx), expected_valid_moves)

                #  0 1 2 3 4 5 6 7
                #0 - - - - - - - -
                #1 - - - - - - - -
                #2 - - - - - - - -
                #3 - - - - - - - -
                #4 - - - - - - - -
                #5 - - - - - - x -
                #6 - - - - - x - -
                #7 - - - - - - - k
                
                k_idx = (7,7)
                expected_valid_moves = {(5,6), (6,5)}
                self.assertEqual(valid_moves(k_idx), expected_valid_moves)

                #  0 1 2 3 4 5 6 7
                #0 - - - - - - - -
                #1 - - x - x - - -
                #2 - x - - - x - -
                #3 - - - k - - - -
                #4 - x - - - x - -
                #5 - - x - x - - -
                #6 - - - - - - - -
                #7 - - - - - - - -
 
                k_idx = (3,3)
                expected_valid_moves = {(1,2), (1,4), (2,1), (2,5), (4,1), (4,5), (5,2), (5,4)}
                self.assertEqual(valid_moves(k_idx), expected_valid_moves)

class TestSolveable(unittest.TestCase):
        def testUnsolveable(self):
                """Test a few unsolveable puzzles"""
                #  0 1 2 3 4 5 6 7
                #0 - - - - - - - -
                #1 - - - - - - - -
                #2 - - - - - - - -
                #3 - - - k - - - -
                #4 - x - - - x - -
                #5 - - - x - - - -
                #6 - - - - - - - -
                #7 - - x - - - - -
 
                k_idx = (3,3) # Initial knight index
                p_idxs = {(1,4),(2,7),(3,5),(5,4)} # Set of pawn indices
                self.assertEqual(solveable(p_idxs, k_idx), False)
        def testSolveableSimple(self):
                """Test a simple solveable puzzle"""
                #  0 1 2 3 4 5 6 7
                #0 - - - - - - - -
                #1 - - - - - - - -
                #2 - - - - - - - -
                #3 - - - k - - - -
                #4 - x - - - x - -
                #5 - - - x - - - -
                #6 - - - - - - - -
                #7 - - - - - - - -
 
                k_idx = (3,3) # Initial knight index
                p_idxs = {(1,4),(3,5),(5,4)} # Set of pawn indices
                self.assertEqual(solveable(p_idxs, k_idx), True)

        def testSolveableHard(self):
                """Test a few more complex solveable puzzles - try to break your recursive algorithm to help you catch any mistakes"""
                #  0 1 2 3 4 5 6 7
                #0 - - - x - - - -
                #1 - - - - - x - -
                #2 - - x - - - - -
                #3 - - - k - - x -
                #4 - x - - - - - -
                #5 - - - - - x - -
                #6 - - x - - - - -
                #7 - - - - x - - -
 
                k_idx = (3,3) # Initial knight index
                p_idxs = {(1,4),(2,6),(4,7),(5,5),(6,3),(5,1),(3,0),(2,2)} # Set of pawn indices
                self.assertEqual(solveable(p_idxs, k_idx), True)

if __name__ == '__main__':
        unittest.main()
        
       