from map import Cell
from map import Maze
from window_builder import Line
from window_builder import Point
from window_builder import Window


def main():
    window_size = Point(800, 800)
    maze_rows_cols = Point(10, 10)
    maze_cell_size = Point(70, 70)
    maze_size = Point(
        maze_rows_cols._x * maze_cell_size._x, maze_rows_cols._y * maze_cell_size._y
    )
    maze_pos = Point(
        (window_size._x - maze_size._x) // 2, (window_size._y - maze_size._y) // 2
    )

    window = Window(window_size._x, window_size._y)
    Maze(maze_pos, maze_cell_size, maze_rows_cols._x, maze_rows_cols._y, window)

    window.wait_for_close()


if __name__ == "__main__":
    main()
