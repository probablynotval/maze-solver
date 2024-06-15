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
        if self.has_left_wall:
            left_wall = Line(Point(p1._x, p1._y), Point(p1._x, p2._y))
            self._window.draw_line(left_wall)
        if self.has_right_wall:
            right_wall = Line(Point(p2._x, p1._y), Point(p2._x, p2._y))
            self._window.draw_line(right_wall)
        if self.has_top_wall:
            top_wall = Line(Point(p1._x, p1._y), Point(p2._x, p1._y))
            self._window.draw_line(top_wall)
        if self.has_bottom_wall:
            bottom_wall = Line(Point(p1._x, p2._y), Point(p2._x, p2._y))
            self._window.draw_line(bottom_wall)

    def draw_move(self, to_cell: "Cell", undo=False):
        if undo:
            self._window.draw_line(self.get_center(), to_cell.get_center(), "gray")
        else:
            self._window.draw_line(self.get_center(), to_cell.get_center(), "red")

    def get_center(self) -> Point:
        center_x = self._x1 + ((self._x2 - self._x1) / 2)
        center_y = self._y1 + ((self._y2 - self._y1) / 2)
        return Point(center_x, center_y)


class Maze:
    def __init__(self, window: Window, pos: Point, size: Point, rows: int, cols: int):
        self._window = window
        self._pos = pos
        self._size = size
        self._rows = rows
        self._cols = cols
        self._create_cells()

    def _create_cells(self):
        self._cells = [
            [Cell(self._window) for _ in range(self._cols)] for _ in range(self._rows)
        ]
        for i in range(self._rows):
            for j in range(self._cols):
                self._draw_cell(Point(i, j))

    def _draw_cell(self, index: Point):
        x_pos = self._pos._x + index._x * self._size._x
        y_pos = self._pos._y + index._y * self._size._y
        self._cells[index._x][index._y]._pos = Point(x_pos, y_pos)
        cell: Cell = self._cells[index._x][index._y]
        cell.draw_walls(
            Point(x_pos, y_pos), Point(x_pos + self._size._x, y_pos + self._size._y)
        )
        self._animate()

    def _animate(self):
        self._window.redraw()
        time.sleep(0.05)
