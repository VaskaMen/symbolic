from PIL.ImageFile import ImageFile

from Image.Segment import Segment


class ImageSlicer:
    @staticmethod
    def get_segments(image: ImageFile, step:int = 10) -> list[Segment]:

        width = image.width
        height = image.height
        segments:  list[Segment] = list()

        for j in range(0, width - step, step):
            segment = Segment(image.crop((j, 0, j + step, height)))
            segments.append(segment)

        return segments

    @staticmethod
    def get_image_lines(image: ImageFile, step: int = 10) -> list[ImageFile]:
        image_lines: list[ImageFile] = []

        height = image.height
        width = image.width

        for i in range(0, height - step, step):
            image_lines.append(image.crop((0, i, width, i + step)))

        return image_lines
