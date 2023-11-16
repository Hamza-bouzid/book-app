import boto3


class S3:
    def __init__(self, region: str, access_key: str, secret_key: str):
        self._s3 = boto3.client(
            "s3",
            region_name=region,
            aws_access_key_id=access_key,
            aws_secret_access_key=secret_key,
        )

    def upload_image_to_s3(self, image_data: bytes, bucket_name: str, object_key: str):
        try:
            self._s3.put_object(
                Bucket=bucket_name,
                Key=object_key,
                Body=image_data,
                ContentType="image/jpeg",
            )

            return f"https://{bucket_name}.s3.amazonaws.com/{object_key}"
        except Exception as e:
            print(f"Failed to upload image to S3: {e}")
            return None
