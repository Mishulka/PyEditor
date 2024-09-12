from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk


class Mixin:
    def open_image(self):
        # открытие изображения для редактирования
        
        filename = filedialog.askopenfilename(title="Выберите файл",
                                              filetypes=(("jpeg файлы", "*.jpg"), ("png файлы", "*.png")))
        if filename:
            self.undo_stack.append(self.image.copy() if self.image else None)  
            self.redo_stack.clear()
            self.image_file = filename
            self.image = Image.open(filename)
            self.image_tk = ImageTk.PhotoImage(self.image)
            self.canvas.create_image(0, 0, anchor=NW, image=self.image_tk)

