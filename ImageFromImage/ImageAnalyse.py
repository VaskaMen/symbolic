import os

from PIL import Image
from rich.progress import Progress

from Image.RGBCountable import RGBCountable
from Image.Segment import Segment


class ImageAnalyse:
    def __init__(self, folder_path: str):
        self.folder_path = folder_path

    def get_all_images(self) -> list[str]:
        return os.listdir(self.folder_path)

    def get_primary_color(self, image_name: str) -> RGBCountable:
        image = Image.open(f"{self.folder_path}/{image_name}")
        segment = Segment(image)
        return segment.get_primary_color()

    def get_all_colors_from_image(self) ->   list[dict[str, RGBCountable | str]]:
        images = self.get_all_images()
        colors = []
        with Progress() as progress:
            task1 = progress.add_task("[green] Анл-лизируем фотографии [#]", total=len(images) -1)

            for i in images:
                primary_color = self.get_primary_color(i)
                colors.append({
                    "RGB": {
                        'R':primary_color.red,
                        'G':primary_color.green,
                        'B':primary_color.blue,
                    },
                    "file": i
                })
                progress.update(task1, advance=1)
        return  colors

