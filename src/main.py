from map import Cell
from map import Maze
from window_builder import Line
from window_builder import Point
from window_builder import Window


def main():
    window = Window(800, 800)
    # window.draw_line(Line(Point(200, 200), Point(800, 800)), "blue")

    # cell = Cell(window)
    # cell.has_bottom_wall = False
    # cell.draw_walls(Point(350, 350), Point(475, 475))

    Maze(window, Point(0, 0), Point(50, 50), 5, 5)

    window.wait_for_close()


if __name__ == "__main__":
    main()
