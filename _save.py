from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk

def Mix(self):
        # конвертация и запись в файл
        if self.image_file and self.image:
            defaultextension = ""
            filetype = ""
            selectedtype = self.image_file.split('.')[-1]
            if selectedtype.lower() == "jpg" or selectedtype.lower() == "jpeg":
                defaultextension = ".jpg"
                filetype = (("JPEG файлы", "*.jpg"),)
            elif selectedtype.lower() == "png":
                defaultextension = ".png"
                filetype = (("PNG файлы", "*.png"),)
            else:
                defaultextension = ".jpg"
                filetype = (("JPEG файлы", "*.jpg"), ("PNG файлы", "*.png"), ("Все файлы", "*.*"))
            filename = filedialog.asksaveasfilename(initialdir="/", title="Сохранить файл как",defaultextension=defaultextension,
                                                    filetypes=filetype)
            if filename:
                if self.image.mode == 'RGBA':
                    self.image = self.image.convert('RGB')
                elif self.image.mode == 'P':
                    self.image = self.image.convert('RGB')
                if filename.endswith('.jpg') or filename.endswith('.jpeg'):
                    self.image.save(filename, 'JPEG', quality=90)
                elif filename.endswith('.png'):
                    self.image.save(filename, 'PNG')
                else:
                    messagebox.showerror("Ошибка!", "Неподдерживаемый формат")