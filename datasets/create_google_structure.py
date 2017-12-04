import os
import optparse
import yaml
import sys
import shutil
import logging

sys.path.append(os.getcwd())

from datasets.pascalvoc_to_tfrecords import *

logging.basicConfig(level=logging.INFO)
LOGGER = logging.getLogger(__name__)

# +data
#   -label_map file
#   -train TFRecord file
#   -eval TFRecord file
# +models
#   + model
#     -pipeline config file
#     +train
#     +eval
def copy_dataset(CONFIG,fname=None):
	des_image = ""
	des_annotation = ""
	write_to_tf_record(CONFIG,fname)

def main(opts):

	CONFIG = yaml.load(open(opts.config))
	ANNOTATION_FOLDER = CONFIG["ANNOTATION_FOLDER"]
	DATA_FOLDER = CONFIG["DATA_FOLDER"]
	N_LABELS = CONFIG["N_LABELS"]
	TRAIN_VAL_FOLDER = CONFIG["TRAIN_VAL_FOLDER"]
	GOOGLE_FOLDER = CONFIG["GOOGLE_FOLDER"]


	try:
		os.makedirs(TRAIN_VAL_FOLDER)
		os.makedirs(os.path.join(TRAIN_VAL_FOLDER,"data"))
		os.makedirs(os.path.join(TRAIN_VAL_FOLDER,"models"))
		os.makedirs(os.path.join(TRAIN_VAL_FOLDER,"models","train"))
		os.makedirs(os.path.join(TRAIN_VAL_FOLDER,"models","val"))
	except Exception as e:
		LOGGER.error(e)

	copy_dataset(CONFIG,opts.file_name)
	# copy_dataset(CONFIG,train=False)


if __name__ == "__main__":
	
	optparser = optparse.OptionParser()
	optparser.add_option("-c", "--config", help="Configuration file", default="")
	optparser.add_option("-f", "--file_name", help="Output name", default="")
	opts = optparser.parse_args()[0]

	main(opts)


