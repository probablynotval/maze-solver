from tkinter import Canvas


class Point:
    def __init__(self, x: float = 0, y: float = 0):
        self._x = x
        self._y = y

    def __repr__(self) -> str:
        return f"Point(x={self._x}px, y={self._y}px)"


class Line:
    def __init__(self, point_1: Point, point_2: Point):
        self._point_1 = point_1
        self._point_2 = point_2

    def _draw(self, canvas: Canvas, fill_color: str):
        canvas.create_line(
            self._point_1._x,
            self._point_1._y,
            self._point_2._x,
            self._point_2._y,
            fill=fill_color,
            width=2,
        )

    def __repr__(self) -> str:
        return f"Line(point_1={self._point_1}, point_2={self._point_2})"
