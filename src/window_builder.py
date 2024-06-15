from tkinter import BOTH
from tkinter import Canvas
from tkinter import Tk

from draw import Line
from draw import Point
from map import Cell


class Window:
    def __init__(
        self, width: int = 1024, height: int = 768, title: str = "Tkinter Window"
    ):
        self._width = width
        self._height = height
        self._root = Tk()
        self._root.protocol("WM_DELETE_WINDOW", self.close)
        self._root.title(title)
        self._canvas = Canvas(self._root, width=self._width, height=self._height)
        self._canvas.pack()
        self._is_running = False

    def redraw(self):
        self._root.update_idletasks()
        self._root.update()

    def wait_for_close(self):
        self._is_running = True
        while self._is_running:
            self.redraw()

    def close(self):
        self._is_running = False

    def draw_line(self, point_1: Point, point_2: Point, fill_color: str):
        Line(point_1, point_2)._draw(self._canvas, fill_color)

    def draw_cell(self, top_left: Point, bottom_right: Point):
        Cell(top_left._x, top_left._y, bottom_right._x, bottom_right._y)._draw(
            self._canvas, top_left, bottom_right
        )
