from Image.RGB import RGB


class ColorWorker:

    @staticmethod
    def json_to_RGB(json: dict) -> RGB:
        return RGB(
            json["R"],
            json["G"],
            json["B"]
        )
