#!/usr/bin/python

import sys

def init():
	cypherTxt = openFile(sys.argv[1])
	

def openFile(fileName):
	txtFile = open(fileName, 'r')
	txt = txtFile.read()
	return txt

if __name__ == '__main__':
	init()