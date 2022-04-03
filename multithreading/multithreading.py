import os
from os import walk
import logging

# from PIL import Image
class CompressOneImage:
    pass

# class who scan the folder and start a thread by image to compress
class ProcessImages:

    def contentsFolder(self):

        for (dirpath, dirnames, filenames) in walk("./bestImages"):
            print("I am the path to the folder:", dirpath)
            print("I am the folders inside this folder:", dirnames)
            print("I am the files inside this folder:", filenames)
    
        for i in filenames:          
            fileName, fileExtension = os.path.splitext(i)
        
        images = [i for i in filenames if fileExtension == ".jpg"]
        print("images jpg only:", images)        

logging.basicConfig(format="%(threadName)s:%(message)s")

ProcessImages().contentsFolder()