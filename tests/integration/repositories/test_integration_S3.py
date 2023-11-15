import pytest

from api import depends


class TestIntegrationS3:

    @pytest.fixture
    def s3(self):
        return depends.get_s3()

    def test_it_should_upload_image_to_s3(self, s3):
        image_data = b'123'
        bucket_name = 'rebelnet'
        object_key = 'test.jpg'

        result = s3.upload_image_to_s3(image_data, bucket_name, object_key)

        assert result is not None
        assert result == f"https://{bucket_name}.s3.amazonaws.com/{object_key}"
