import os
import re

import cv2
from rich.progress import Progress

from FileWorker import FileWorker
from VideoStudio.SymbolImageCreator import SymbolImageCreator
from VideoStudio.SymbolImageCreatorParams import SymbolImageCreatorParams


class VideoCreator:

    @staticmethod
    def create_symbol_frames(quality: int, settings: SymbolImageCreatorParams = SymbolImageCreatorParams()):
        FileWorker.delete_files_in_folder('VideoStudio/symbol_frames')
        files_len = len(os.listdir('VideoStudio/frames'))
        with Progress() as progress:
            task1 = progress.add_task(f"[green] Создаём кадры из символов [#]", total=files_len - 1)

            for i in range(0, files_len):
                creator = SymbolImageCreator(f'VideoStudio/frames\\frame_{i}.jpg', settings)
                creator.make_image_symbolic(quality)
                creator.save_image(path='VideoStudio/symbol_frames')

                progress.update(task1, advance=1)

    @staticmethod
    def make_video(fps: int = 30, image_folder: str = 'VideoStudio/symbol_frames'):

        def extract_number(file_name):
            return int(re.search(r'_(\d+)', file_name).group(1))



        video_name = 'output_video.mp4'

        # images = [img for img in os.listdir(image_folder) if img.endswith(".jpg") or img.endswith(".png")]
        images = os.listdir(image_folder)
        images = sorted(images, key=extract_number)

        first_image = cv2.imread(os.path.join(image_folder, images[0]))
        height, width, layers = first_image.shape

        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        video = cv2.VideoWriter(video_name, fourcc, fps, (width, height))

        with Progress() as progress:
            task1 = progress.add_task(f"[green] Склеиваем видио [#]", total=len(images) -1)
            for image in images:
                video.write(cv2.imread(os.path.join(image_folder, image)))
                progress.update(task1, advance=1)
        video.release()
        cv2.destroyAllWindows()

    @staticmethod
    def get_all_image_path(image_folder: str) -> list[str]:
        return [img for img in os.listdir(image_folder) if img.endswith(".jpg") or img.endswith(".png")]


