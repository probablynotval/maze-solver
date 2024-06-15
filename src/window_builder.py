from tkinter import Tk, BOTH, Canvas


class Window:
    def __init__(self, width: int = 800, height: int = 600, title: str = "Tkinter Window"):
        self.width = width
        self.height = height
        self.__root = Tk()
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        self.__root.title(title)
        self.canvas = Canvas(self.__root, width=self.width, height=self.height)
        self.canvas.pack()
        self.is_running = False

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.is_running = True
        while self.is_running:
            self.redraw()

    def close(self):
        self.is_running = False

