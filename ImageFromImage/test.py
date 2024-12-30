import os

from ImageFromImage.ImageFromImageCreator import ImageFromImageCreator


im = ImageFromImageCreator('../l.jpg')
im.make_image_from_image(8, upscale=12)
im.save_image(os.path.dirname(os.path.abspath(__file__)))

