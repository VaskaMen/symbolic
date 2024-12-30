import os
import tkinter as tk
from tkinter import filedialog


from rich.console import Console

from ImageFromImage.ImageFromImageCreator import ImageFromImageCreator
from SymbolicImage.SymbolImageCreator import SymbolImageCreator
from SymbolicImage.SymbolImageCreatorParams import SymbolImageCreatorParams
from VideoStudio.VideoCreator import VideoCreator
from VideoStudio.VideoCapture import VideoCapture


console = Console()

root = tk.Tk()
root.withdraw()

console.print("[white]0# Фотографии")
console.print("[white]1# Видео")
console.print("[white]2# Фотография из фотографий")

index = int(console.input('[yellow]Выберите режим работы (укажите номер): '))

if index == 0:
    console.print("[green]Укажите путь к фотографии...")
    path = filedialog.askopenfile(filetypes=[("Images", "*.jpg")]).name

    qu = int(console.input("Степень детализации [red] \n (малые значения могут сильно сказаться на времени обработки): "))
    font_size = int(console.input("Размер шрифта: "))
    symbols = console.input("Какие симолы использовать (через пробел): ").split(' ')
    ran = console.input("Брать рандомный символ да/нет: ") == 'да'

    settings = SymbolImageCreatorParams()
    settings.set_font_size(font_size)
    settings.set_use_symbol(symbols)
    settings.take_random_symbol = ran


    creator = SymbolImageCreator(path, settings)
    creator.make_image_symbolic(qu)
    creator.save_image(os.path.dirname(os.path.abspath(__file__)))
    console.print("[green]Завершено")

if index == 1:
    console.print("[green]Укажите путь к видео файл...")
    path = filedialog.askopenfile(filetypes=[("Video", "*.mp4")]).name
    fps = int(console.input("Брать каждый n кадр: "))
    font_size = int(console.input("Размер шрифта: "))
    symbols = console.input("Какие симолы использовать (через пробел): ").split(' ')
    ran = console.input("Брать рандомный символ да/нет: ") == 'да'
    qu = int(console.input("Степень детализации [red] \n (малые значения могут сильно сказаться на времени обработки): "))

    cap = VideoCapture(path)
    cap.take_frame_from_video(fps)
    params = SymbolImageCreatorParams()
    params.set_new_font('VideoStudio/noto.ttf')
    params.set_font_size(font_size)
    params.set_use_symbol(symbols)
    params.take_random_symbol = ran
    VideoCreator.create_symbol_frames(qu, params)
    VideoCreator.make_video()
    console.print("[green]Завершено")


if index == 2:
    console.print("[green]Укажите путь к файлу...")
    path = filedialog.askopenfile(filetypes=[("Images", "*.jpg")]).name
    console.print("[red] Поместите фотографии в папку ImageFromImage/used_images")
    console.print("[red] ТОЛЬКО .JPG !!!")

    qu = int(console.input("Качество: "))
    up = int(console.input("Upscale: "))


    im = ImageFromImageCreator(path)
    im.make_image_from_image(qu, upscale=up)
    im.save_image(os.path.dirname(os.path.abspath(__file__)))
    console.print("[green]Завершено")




