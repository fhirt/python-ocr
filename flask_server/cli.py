import sys
from ocr import process_image

if __name__ == '__main__':
    sys.stdout.write("""
===OOOO=====CCCCC===RRRRRR=====\n
==OO==OO===CC=======RR===RR====\n
==OO==OO===CC=======RR===RR====\n
==OO==OO===CC=======RRRRRR=====\n
==OO==OO===CC=======RR==RR=====\n
==OO==OO===CC=======RR== RR====\n
===OOOO=====CCCCC===RR====RR===\n\n
""")
    sys.stdout.write("A simple OCR utility\n")
    url = input("What is the url of the image you would like to analyze?\n")
    sys.stdout.write("The raw output from tesseract with no processing is:\n\n")
    sys.stdout.write("-----------------BEGIN-----------------\n")
    sys.stdout.write(process_image(url) + "\n")
    sys.stdout.write("------------------END------------------\n")