from PIL.ImageFile import ImageFile

from Image.ImageSlicer import ImageSlicer
from Image.Segment import Segment


class SegmentedImage:
    segments: list[list[Segment]]

    def __init__(self, image: ImageFile, step: int):
        segments: list[list[Segment]] = list()
        lines = ImageSlicer.get_image_lines(image, step)
        for line in lines:
            segment = ImageSlicer.get_segments(line, step)
            segments.append(segment)
        self.segments = segments