from config import get_config
from maze import Maze
from start_vnc import setup_vnc
from window_builder import Point
from window_builder import Window


def main():
    config = get_config()
    if config["vnc"]["bool"] == True:
        setup_vnc()
    window_size = Point(config["window"]["width"], config["window"]["height"])
    maze_rows_cols = Point(config["grid"]["columns"], config["grid"]["rows"])
    maze_cell_size = Point(config["grid"]["size_x"], config["grid"]["size_y"])
    maze_size = Point(
        maze_rows_cols._x * maze_cell_size._x, maze_rows_cols._y * maze_cell_size._y
    )
    maze_pos = Point(
        (window_size._x - maze_size._x) // 2, (window_size._y - maze_size._y) // 2
    )

    window = Window(window_size._x, window_size._y)
    Maze(maze_pos, maze_cell_size, maze_rows_cols._x, maze_rows_cols._y, window).solve()

    window.wait_for_close()


if __name__ == "__main__":
    main()
