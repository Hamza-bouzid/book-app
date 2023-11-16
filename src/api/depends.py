import os

from dotenv import load_dotenv

from controller.BookController import BookController
from controller.DownloadController import DownloaderController
from controller.UploadImageController import UploadImageController
from repositories.DownloadImage import DownloadImage
from repositories.DynamoDB import DynamoDB
from repositories.S3 import S3

load_dotenv()


def get_book_controller() -> BookController:
    upload_image_controller = get_upload_image_controller()
    download_controller = get_downloader_controller()
    db = get_db()
    return BookController(
        upload_image_controller=upload_image_controller,
        download_controller=download_controller,
        db=db,
    )


def get_upload_image_controller() -> UploadImageController:
    s3 = get_s3()
    return UploadImageController(s3=s3)


def get_s3() -> S3:
    return S3(
        region=os.getenv("AWS_REGION"),
        access_key=os.getenv("AWS_ACCESS_KEY"),
        secret_key=os.getenv("AWS_SECRET_KEY"),
    )


def get_downloader_controller() -> DownloaderController:
    return DownloaderController(download_image=DownloadImage())


def get_db():
    return DynamoDB(book_table=os.getenv("BOOK_TABLE"))
