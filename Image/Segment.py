from PIL.Image import Image
from PIL.ImageFile import ImageFile

from Image.RGBCountable import RGBCountable


class Segment:

    segment: ImageFile | Image

    def __init__(self, segment: ImageFile | Image):
        self.segment = segment

    def get_colors_segment(self) -> list[RGBCountable]:
        crgb_list: list[RGBCountable] = list()
        size = self.segment.width * self.segment.height
        color_list = self.segment.getcolors(maxcolors=size)
        for i in color_list:
            crgb_list.append(RGBCountable(i))

        return crgb_list

    def get_primary_color(self) -> RGBCountable:
        colors = self.get_colors_segment()
        often_color: RGBCountable = colors[0]

        for i in colors:
            if i.count > often_color.count:
                often_color = i
        return often_color