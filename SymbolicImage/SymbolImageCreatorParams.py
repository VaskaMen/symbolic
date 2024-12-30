from PIL import ImageFont

from settings import default_font_path


class SymbolImageCreatorParams:

    __font_size = 10
    __font_path: str = default_font_path
    font = ImageFont.truetype(__font_path, size=__font_size)
    use_symbol: list[str] = ["#"]

    take_random_symbol: bool = True

    def set_new_font(self, font_path: str, ):
        self.__font_path = font_path
        self.font = ImageFont.truetype(font_path, size=self.__font_size)

    def set_font_size(self, size: int):
        self.font = ImageFont.truetype(self.__font_path, size=size)

    def set_use_symbol(self, symbol: list[str]):
        self.use_symbol = symbol