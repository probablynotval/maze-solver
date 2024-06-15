from tkinter import BOTH
from tkinter import Canvas
from tkinter import Tk

from draw import Line
from draw import Point


class Window:
    def __init__(
        self, width: int = 1024, height: int = 768, title: str = "Tkinter Window"
    ):
        self._root = Tk()
        self._root.protocol("WM_DELETE_WINDOW", self.close)
        self._root.title(title)
        self._canvas = Canvas(self._root, bg="white", width=width, height=height)
        self._canvas.pack(fill=BOTH, expand=1)
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

    def draw_line(self, line: Line, fill_color: str = "black"):
        line._draw(self._canvas, fill_color)

    # def draw_cell(self, top_left: Point, bottom_right: Point):
    #     Cell()._draw(self._canvas, top_left, bottom_right)
