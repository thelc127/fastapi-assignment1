import pytesseract
import requests
from PIL import Image
from PIL import ImageFilter
#from StringIO import StringIO


def _get_image(url):
    return Image.open(requests.get(url).content)
 
def process_image(url):
    image = _get_image(url)
    image.filter(ImageFilter.SHARPEN)
    return pytesseract.image_to_string(image)
 
