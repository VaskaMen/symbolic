import os

from PIL import Image, ImageDraw

from settings import symbol_image_prefix


class ImageCreator:

    def __init__(self, path: str):
        self.image = Image.open(path)
        self.file_name = os.path.basename(self.image.filename)

    def save_image(self, path: str = '', rewrite_image: bool = False):
        if not rewrite_image:
            self.image.save(f'{path}\\{symbol_image_prefix}{self.file_name}')
        else:
            self.image.save(self.image.filename)