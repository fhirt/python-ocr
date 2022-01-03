import pytesseract
import requests
from PIL import Image, ImageFilter

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


def process_image(url):
    image = _get_image(url)
    image = image.convert('RGB')
    image = image.filter(ImageFilter.SHARPEN)
    return pytesseract.image_to_string(image)


def _get_image(url):
    if url.startswith('http'):
        response = requests.get(url, stream=True)
        return Image.open(response.raw)
    else:
        return Image.open(url)
