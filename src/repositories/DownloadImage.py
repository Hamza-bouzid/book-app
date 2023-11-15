import requests


class DownloadImage:
    @staticmethod
    def download_image(image_url) -> bytes | None:
        response = requests.get(image_url)
        if response.status_code == 200:
            return response.content
        return None
