from tkinter import Tk, Canvas


class Window:
    def __init__(self, width: int = 800, height: int = 600, title: str = "Tkinter Window"):
        self.width = width
        self.height = height
        self.root = Tk()
        self.root.title(title)
        self.canvas = Canvas(self.root, width=self.width, height=self.height)
        self.canvas.pack()
        self.is_running = False