from draw import Point
from window_builder import Window


def main():
    window = Window()
    window.draw_line(Point(200, 200), Point(800, 800), "blue")
    window.draw_cell(Point(200, 200), Point(400, 400))
    window.wait_for_close()


if __name__ == "__main__":
    main()
