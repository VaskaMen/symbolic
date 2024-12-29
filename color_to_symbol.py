import os

from PIL import Image
from rich.progress import Progress

from Image.SegmentedImage import SegmentedImage


def color_text(hex: str, text: str, ignor_hex: str = "#64ef18"):
    if hex == ignor_hex:
        return ' '
    return f'[{hex}]{text}'

def count_frames(folder: str) -> int:
    return len(os.listdir(folder))

def create_symbol_frame(folder: str, quality:int = 10, crop: tuple[int, int, int, int] | None = None) -> [str]:
    total_frames = count_frames(folder)

    with Progress() as progress:
        task1 = progress.add_task("[green] Создаём символы [#]", total=total_frames-1)

        frames: [str] = []
        for f in range(0, total_frames - 1):
            image = Image.open(f'{folder}\\frame_{f}.jpg')

            if crop is not None:
                image=image.crop(crop)

            symbol = SegmentedImage(image, quality)
            line = " "
            for i in symbol.segments:
                for j in i:
                    line += color_text(j.get_primary_color().to_hex(), "█")
                line += "\n"
            frames.append(line)
            progress.update(task1, advance=1)
    return frames
