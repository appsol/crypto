#!/usr/bin/python

from PIL import Image
from pytesseract import *

def getImageText(imgFilePath):
	textImage = Image.open(imgFilePath)
	imageText = image_to_string(textImage)
	print imageText

def init():
	getImageText()

if __name__ == "__main__":
	import sys
	getImageText(sys.argv[1])