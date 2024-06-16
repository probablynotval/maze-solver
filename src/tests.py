import unittest

from maze import Cell
from maze import Maze
from window_builder import Point


class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(Point(0, 0), Point(10, 10), num_rows, num_cols)
        self.assertEqual(
            len(m1._cells),
            num_rows,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_cols,
        )

    def test_maze_break_entrance_and_exit(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(Point(0, 0), Point(10, 10), num_rows, num_cols)
        self.assertEqual(
            m1._cells[0][0].has_top_wall,
            False,
        )
        self.assertEqual(
            m1._cells[num_rows - 1][num_cols - 1].has_bottom_wall,
            False,
        )

    def test_cell_visit_reset(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(Point(0, 0), Point(10, 10), num_rows, num_cols)
        visited = []
        for i in range(num_rows):
            for j in range(num_cols):
                visited.append(m1._cells[i][j].visited)
        self.assertEqual(all(value == False for value in visited), True)


if __name__ == "__main__":
    unittest.main()
