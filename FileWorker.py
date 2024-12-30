import os


class FileWorker:

    @staticmethod
    def delete_files_in_folder(folder_path):
        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)
            try:
                if os.path.isfile(file_path):
                    os.remove(file_path)
            except Exception as e:
                print(f'Ошибка при удалении файла {file_path}. {e}')

    @staticmethod
    def create_folder(folder_path: str):
        file_exist = os.path.exists(folder_path)
        if not file_exist:
            os.mkdir(folder_path)