from PIL.Image import Image
from PIL import Image as ImageF
from PIL import ImageDraw
from rich.progress import Progress

from Image.SegmentedImage import SegmentedImage
from ImageFromImage.ImageAnalyse import ImageAnalyse
from ImageFromImage.SelectImage import SelectImage
from SymbolicImage.ImageCreator import ImageCreator


class ImageFromImageCreator(ImageCreator):

    def make_image_from_image(self, quality: int, upscale: int =1):
        segments = SegmentedImage(self.image, quality)
        new_image: Image = ImageF.new('RGB', (self.image.width*upscale, self.image.height*upscale), 'black')

        idraw = ImageDraw.Draw(new_image)

        analyse = ImageAnalyse('ImageFromImage/used_images').get_all_colors_from_image()

        x = 0
        y = 0
        with Progress() as progress:
            task1 = progress.add_task("[green] Клеим картинки [#]", total=len(segments.segments))

            for line in segments.segments:
                for segment in line:
                    segment_primary_color = segment.get_primary_color()
                    select = SelectImage(analyse)
                    image_name = select.get_closest_image_to_RGB(segment_primary_color)
                    image = ImageF.open(f'ImageFromImage/used_images/{image_name}')
                    image = image.resize((quality*upscale,quality*upscale))
                    Image.paste(new_image, image, (x, y))
                    x += quality*upscale

                x = 0
                y += quality*upscale
                progress.update(task1, advance=1)
        self.image = new_image