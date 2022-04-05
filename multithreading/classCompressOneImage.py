import os
import logging
from pickletools import optimize
from PIL import Image

class CompressOneImage:

    def __init__(self):

        compressedImagefilepath = "./bestImages/compressedImages"
        if not os.path.exists(compressedImagefilepath):
            print("The folder doesn't exists, I will create it !")
            os.makedirs(compressedImagefilepath)
        else:
            print("It's okay! The directory already exists!")

        imageFilepath = "./bestImages/bebou.jpg"
        picture = Image.open(imageFilepath)
        print("I am opening the image")

        imageFilesize = os.stat(imageFilepath).st_size
        print("I am get size of this image:", imageFilesize, "bytes")

        picture.save("compressed.jpg", "JPEG", optimize=True, quality=30)
        print("I am compressing the image selected")

        

    logging.basicConfig(format="%(threadName)s:%(message)s")

CompressOneImage()