import time

from draw import Line
from draw import Point
from window_builder import Window


class Cell:
    def __init__(self, window: Window):
        self._window = window
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = None
        self._y1 = None
        self._x2 = None
        self._y2 = None

    def draw_walls(self, p1: Point, p2: Point):
        self._x1 = p1._x
        self._y1 = p1._y
        self._x2 = p2._x
        self._y2 = p2._y

        left_wall = Line(Point(p1._x, p1._y), Point(p1._x, p2._y))
        right_wall = Line(Point(p2._x, p1._y), Point(p2._x, p2._y))
        top_wall = Line(Point(p1._x, p1._y), Point(p2._x, p1._y))
        bottom_wall = Line(Point(p1._x, p2._y), Point(p2._x, p2._y))

        if self.has_left_wall:
            self._window.draw_line(left_wall)
        elif self.has_left_wall == False:
            self._window.draw_line(left_wall, "white")

        if self.has_right_wall:
            self._window.draw_line(right_wall)
        elif self.has_right_wall == False:
            self._window.draw_line(right_wall, "white")

        if self.has_top_wall:
            self._window.draw_line(top_wall)
        elif self.has_top_wall == False:
            self._window.draw_line(top_wall, "white")

        if self.has_bottom_wall:
            self._window.draw_line(bottom_wall)
        elif self.has_bottom_wall == False:
            self._window.draw_line(bottom_wall, "white")

    def draw_move(self, to_cell: "Cell", undo=False):
        if undo:
            self._window.draw_line(self.get_center(), to_cell.get_center(), "gray")
        else:
            self._window.draw_line(self.get_center(), to_cell.get_center(), "red")

    def get_center(self) -> Point:
        center_x = self._x1 + ((self._x2 - self._x1) / 2)
        center_y = self._y1 + ((self._y2 - self._y1) / 2)
        return Point(center_x, center_y)

    def __repr__(self) -> str:
        return (
            f"Cell("
            f"has_left_wall={self.has_left_wall}, "
            f"has_right_wall={self.has_right_wall}, "
            f"has_top_wall={self.has_top_wall}, "
            f"has_bottom_wall={self.has_bottom_wall}, "
            f"x1={self._x1}, y1={self._y1}, "
            f"x2={self._x2}, y2={self._y2})"
        )


class Maze:
    def __init__(
        self, pos: Point, size: Point, rows: int, cols: int, window: Window = None
    ):
        self._cells = []
        self._pos = pos
        self._size = size
        self._rows = rows
        self._cols = cols
        self._window = window

        self._create_cells()
        # self._break_entrance_and_exit()

    def _create_cells(self):
        self._cells = [
            [Cell(self._window) for _ in range(0, self._cols)]
            for _ in range(0, self._rows)
        ]
        for i in range(self._rows):
            for j in range(self._cols):
                self._draw_cell(Point(i, j))

    def _draw_cell(self, index: Point):
        if self._window is None:
            return
        x_pos = self._pos._x + index._x * self._size._x
        y_pos = self._pos._y + index._y * self._size._y
        cell: Cell = self._cells[index._x][index._y]
        if index._x == 0 and index._y == 0:
            cell = self._cells[index._x][index._y]
            cell.has_top_wall = False
        else:
            cell.has_top_wall = True

        if index._x == self._rows - 1 and index._y == self._cols - 1:
            cell = self._cells[index._x][index._y]
            cell.has_bottom_wall = False
        else:
            cell.has_bottom_wall = True

        cell: Cell = self._cells[index._x][index._y]
        cell.draw_walls(
            Point(x_pos, y_pos), Point(x_pos + self._size._x, y_pos + self._size._y)
        )
        # if index._x != 0 and index._y != 0 or index._x != self._rows - 1 and index._y != self._cols - 1:
        self._animate()

    def _animate(self):
        if self._window is None:
            return
        self._window.redraw()
        time.sleep(1.5 / (self._rows * self._cols))

    # def _break_entrance_and_exit(self):
    #     self._cells[0][0].has_top_wall = False
    #     self._draw_cell(Point(0, 0))
    #     self._cells[self._rows - 1][self._cols - 1].has_bottom_wall = False
    #     self._draw_cell(Point(self._rows - 1, self._cols - 1))
