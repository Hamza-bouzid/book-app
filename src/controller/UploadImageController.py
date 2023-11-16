from src.repositories.S3 import S3


class UploadImageController:
    def __init__(self, s3: S3):
        self.s3 = s3

    def upload_image_to_s3(
        self, image_data: bytes, bucket_name: str, object_key: str
    ) -> bool:
        try:
            self.s3.upload_image_to_s3(image_data, bucket_name, object_key)
            return True
        except Exception as e:
            print(f"Failed to upload image to S3: {e}")
            return False
