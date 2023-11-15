import logging

from src.repositories.DownloadImage import DownloadImage


class DownloaderController:
    def __init__(self, download_image: DownloadImage):
        self.download_image = download_image

    def download_image(self, url) -> bytes:
        try:
            image = self.download_image.download_image(url)
            return image
        except Exception as e:
            logging.error('DownloaderController - download_image - Error downloading image\n{}'.format(e))
