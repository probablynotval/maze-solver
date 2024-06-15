from tkinter import Tk, BOTH, Canvas


class Window:
    def __init__(self, width: int = 800, height: int = 600, title: str = "Tkinter Window"):
        self.__width = width
        self.__height = height
        self.__root = Tk()
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        self.__root.title(title)
        self.__canvas = Canvas(self.__root, width=self.__width, height=self.__height)
        self.__canvas.pack()
        self.__is_running = False

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.__is_running = True
        while self.__is_running:
            self.redraw()

    def close(self):
        self.__is_running = False

