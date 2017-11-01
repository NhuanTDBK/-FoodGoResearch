import os
import optparse
import logging
import yaml
import sys
import shutil
import glob

logging.basicConfig(level=logging.INFO)
LOGGER = logging.getLogger(__name__)

CONFIG = yaml.load(open(sys.argv[1]))
ANNOTATION_FOLDER = CONFIG["ANNOTATION_FOLDER"]
IMAGE_FOLDER = CONFIG["IMAGE_FOLDER"]
DATA_FOLDER = CONFIG["DATA_FOLDER"]
N_LABELS = CONFIG["N_LABELS"]

def copy_to_folder(folder_path):
	list_files = glob.glob("%s/*.jpg"%folder_path)
	for file in list_files:
		LOGGER.info(file)
		shutil.copy(file,IMAGE_FOLDER)

def main():
	try:
		os.mkdir(IMAGE_FOLDER)
	except:
		print "Folder existed"
	for idx in range(1,N_LABELS+1):
		copy_to_folder("{ROOT}/{INDEX}".format(ROOT=DATA_FOLDER,
			IMAGE_FOLDER=IMAGE_FOLDER,
			INDEX=idx))
		
if __name__ == "__main__":

	main()