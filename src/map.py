from tkinter import Canvas

from draw import Line
from draw import Point


class Cell:
    def __init__(
        self, x1, y1, x2, y2, win=True, left=True, right=True, top=True, bottom=True
    ):
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2
        self._win = win
        self.has_left_wall = left
        self.has_right_wall = right
        self.has_top_wall = top
        self.has_bottom_wall = bottom

    # there might be a better way to implement the canvas while still specifying type
    # could perhaps re-export this in window_builder
    def _draw(self, canvas: Canvas, top_left: Point, bottom_right: Point):
        if self.has_left_wall:
            Line(
                Point(top_left._x, top_left._y), Point(top_left._x, bottom_right._y)
            )._draw(canvas, "black")
        if self.has_right_wall:
            Line(
                Point(bottom_right._x, top_left._y),
                Point(bottom_right._x, bottom_right._y),
            )._draw(canvas, "black")
        if self.has_top_wall:
            Line(
                Point(top_left._x, top_left._y), Point(bottom_right._x, top_left._y)
            )._draw(canvas, "black")
        if self.has_bottom_wall:
            Line(
                Point(top_left._x, bottom_right._y),
                Point(bottom_right._x, bottom_right._y),
            )._draw(canvas, "black")
