from src.repositories.DownloadImage import DownloadImage


def test_it_should_download_image():
    image_url = "https://images-na.ssl-images-amazon.com/images/I/51Zymoq7UnL._SX327_BO1,204,203,200_.jpg"

    download_image = DownloadImage()
    response = download_image.download_image(image_url)

    assert response is not None
