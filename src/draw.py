from tkinter import Canvas


class Point:
    def __init__(self, x: float = 0, y: float = 0):
        self._x = x
        self._y = y

    def __repr__(self) -> str:
        return f"Point(x={self._x}px, y={self._y}px)"


class Line:
    def __init__(self, p1: Point, p2: Point):
        self._p1 = p1
        self._p2 = p2

    def _draw(self, canvas: Canvas, fill_color: str):
        canvas.create_line(
            self._p1._x,
            self._p1._y,
            self._p2._x,
            self._p2._y,
            fill=fill_color,
            width=2,
        )

    def __repr__(self) -> str:
        return f"Line(p1={self._p1}, p2={self._p2})"
