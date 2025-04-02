import unittest
from maze import Maze
from graphics import *  

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        win = Window(800, 600)

        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10, win)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )

        # Destroy win
        win.destroy() 

    def test_maze_create_cells_different_dimensions(self):
        win = Window(800, 600)
        num_cols = 5
        num_rows = 8
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10, win)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )

        # Destroy win
        win.destroy() 

    def test_maze_break_entrance_and_exit(self):
        win = Window(800, 600)

        num_cols = 5
        num_rows = 8
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10, win)
        m1._break_entrance_and_exit()
        self.assertFalse(m1._cells[0][0].has_top_wall)
        self.assertFalse(m1._cells[num_cols - 1][num_rows - 1].has_bottom_wall)

        # Destroy win
        win.destroy() 

    def test_reset_cells_visited(self):
        win = Window(800, 600)

        num_cols = 5
        num_rows = 8
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10, win)
        m1._cells[0][0].visited = True
        m1._reset_cells_visited()
        self.assertFalse(m1._cells[0][0].visited)

        # Destroy win
        win.destroy() 

if __name__ == "__main__":
    unittest.main()

