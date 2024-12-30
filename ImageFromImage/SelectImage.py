import random

from Image.RGB import RGB
from ImageFromImage.ColorWorker import ColorWorker


class SelectImage:

    def __init__(self, image_analyse_result: dict):
        self.images = image_analyse_result

    def get_closest_image_to_RGB(self, color: RGB) -> str:
        closest = []
        dif = 777
        for image in self.images:
            image_color = ColorWorker.json_to_RGB(image["RGB"])
            curent_dif = color.get_difference(image_color)
            if curent_dif < dif:
                dif = curent_dif
                closest.insert(0, image['file'])
        return closest[0]
