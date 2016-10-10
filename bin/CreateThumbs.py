import re
import os
import sys
from PIL import Image
from optparse import OptionParser

class CreateThumbs:

	def __init__(self, inputFolder, outputFolder):

		filePaths = []

		for root, directories, files in os.walk(inputFolder):
			for filename in files:
				filepath = os.path.join(root, filename)
				filePaths.append(filepath)  		

		for filename in filePaths:
			self.createThumbnail(filename, outputFolder)

		self.createIndex(filePaths, outputFolder)


	def createIndex(self, inputFilePaths, outputFolder):

		outputText  = '<html>\n'
		outputText += '  <body>\n'

		for imageFilename in inputFilePaths:
			inputFilename = imageFilename.split('/')[-1]
			outfile     = os.path.splitext(inputFilename)[0] + "_thumbs.jpg"
			outpath     = outputFolder + '/' + outfile
			outputText += ' <a href="{0}">'.format(inputFilename)
			outputText += ' <img src="{0}">'.format(outfile)
			outputText += ' </a>\n'.format(imageFilename)
	

		outputText += '  </body>\n'
		outputText += '</html>\n'
		print outputText				

	def createThumbnail(self, imageFilename, outputFolder):
		size = 128, 128
		
		inputFilename = imageFilename.split('/')[-1]
		outfile = os.path.splitext(inputFilename)[0] + "_thumbs.jpg"
		outpath = outputFolder + '/' + outfile
		if imageFilename != outfile:
			try:
				im = Image.open(imageFilename)
				im.thumbnail(size)
				im.save(outpath, "JPEG")
			except IOError, err:
				print "cannot create thumbnail for", imageFilename
				print str(err)
def main(argv):
	parser = OptionParser(usage="Usage: CreateThumbs <input_folder> <output_folder>")

        parser.add_option("-v", "--verbose",
                action="store_true",
                dest="verboseFlag",
                default=False,
                help="Verbose output from the script")

	(options, filename) = parser.parse_args()

	if len(filename) != 2 or not os.path.isdir(filename[0]) or not os.path.isdir(filename[0]):
		parser.print_help()
		exit(1)

	creatThumbs = CreateThumbs(filename[0], filename[1])
	
if __name__ == "__main__":
    sys.exit(main(sys.argv))
