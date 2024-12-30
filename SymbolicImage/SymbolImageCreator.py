import os
import random

from PIL import Image, ImageDraw

from Image.SegmentedImage import SegmentedImage
from SymbolicImage.ImageCreator import ImageCreator
from SymbolicImage.SymbolImageCreatorParams import SymbolImageCreatorParams
from settings import symbol_image_prefix


class SymbolImageCreator(ImageCreator):
    __last_used_symbol: int = 0


    def __init__(self, path: str, settings: SymbolImageCreatorParams = SymbolImageCreatorParams()):
        super().__init__(path)
        self.settings = settings

    def set_settings(self, settings: SymbolImageCreatorParams):
        self.settings = settings

    def make_image_symbolic(self, quality: int):
        segmented_image = SegmentedImage(self.image, quality)
        new_image: Image = Image.new('RGB', (self.image.width, self.image.height), 'black')
        idraw = ImageDraw.Draw(new_image)

        x = 0
        y = 0

        for line in segmented_image.segments:
            for segment in line:
                color = segment.get_primary_color().to_hex()
                idraw.text(xy=(x, y), text=self.__take_symbol(), font=self.settings.font, fill=color)
                x += quality
            x = 0
            y += quality
        self.image = new_image

    def __take_symbol(self) -> str:
        if self.settings.take_random_symbol:
            return self.__take_random_symbol()
        else:
            return  self.__take_symbol_in_order()

    def __take_random_symbol(self) -> str:
        return random.choice(self.settings.use_symbol)

    def __take_symbol_in_order(self) -> str:
        if self.__last_used_symbol <= len(self.settings.use_symbol) - 1:
            symbol = self.settings.use_symbol[self.__last_used_symbol]
            self.__last_used_symbol += 1
            return symbol
        else:
            self.__last_used_symbol = 0
            symbol = self.settings.use_symbol[self.__last_used_symbol]
            self.__last_used_symbol += 1
            return symbol