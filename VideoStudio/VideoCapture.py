import cv2
from rich.progress import Progress

from FileWorker import FileWorker


class VideoCapture:
    def __init__(self, path: str):
        self.path = path
        self.file_name = path.split('.')[0]
        self.cap = cv2.VideoCapture(self.path)

        self.fps = self.cap.get(cv2.CAP_PROP_FPS)
        self.frame_count = int(self.cap.get(cv2.CAP_PROP_FRAME_COUNT))
        self.duration = self.frame_count / self.fps


    def take_frame_from_video(self, ever_frame:int = 60):
        FileWorker.delete_files_in_folder("VideoStudio/frames")
        with Progress() as progress:
            task1 = progress.add_task("[green] Генерируем кадры [#]", total=self.frame_count)

            frame_number = 0
            img_number = 0

            while True:
                ret, frame = self.cap.read()
                if not ret:
                    break
                if frame_number % ever_frame == 0:
                    cv2.imwrite(f"VideoStudio\\frames\\frame_{img_number}.jpg", frame)
                    img_number += 1

                frame_number += 1
                progress.update(task1, advance=1)
            self.cap.release()


