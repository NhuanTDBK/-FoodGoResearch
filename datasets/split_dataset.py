import os
import optparse
import yaml
import sys
import shutil
import logging


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
def copy_dataset(rows,CONFIG,train=True):
	des_image = ""
	des_annotation = ""
	TRAIN_VAL_FOLDER = CONFIG["TRAIN_VAL_FOLDER"]
	ANNOTATION_FOLDER = CONFIG["ANNOTATION_FOLDER"]
	if train:
		des_image = os.path.join(TRAIN_VAL_FOLDER,"train","JPEGImages")
		des_annotation = os.path.join(TRAIN_VAL_FOLDER,"train","Annotations")
	else:
		des_image = os.path.join(TRAIN_VAL_FOLDER,"val","JPEGImages")
		des_annotation = os.path.join(TRAIN_VAL_FOLDER,"val","Annotations")

	for row in rows:
		src = row.strip()
		LOGGER.info("Processing %s",row)
		shutil.copy(src,des_image)


	for row in rows:
		src = os.path.join(ANNOTATION_FOLDER,row.strip().split("/")[-1].split(".")[0]+".xml")	
		LOGGER.info("Processing %s",row)
		shutil.copy(src,des_annotation)		


def main(opts):

	CONFIG = yaml.load(open(opts.config))
	ANNOTATION_FOLDER = CONFIG["ANNOTATION_FOLDER"]
	DATA_FOLDER = CONFIG["DATA_FOLDER"]
	N_LABELS = CONFIG["N_LABELS"]
	TRAIN_VAL_FOLDER = CONFIG["TRAIN_VAL_FOLDER"]

	try:
		os.makedirs(TRAIN_VAL_FOLDER)
		os.makedirs(os.path.join(TRAIN_VAL_FOLDER,"train"))
		os.makedirs(os.path.join(TRAIN_VAL_FOLDER,"val"))
		os.makedirs(os.path.join(TRAIN_VAL_FOLDER,"train","Annotations"))
		os.makedirs(os.path.join(TRAIN_VAL_FOLDER,"train","JPEGImages"))
		os.makedirs(os.path.join(TRAIN_VAL_FOLDER,"val","Annotations"))
		os.makedirs(os.path.join(TRAIN_VAL_FOLDER,"val","JPEGImages"))
	except Exception as e:
		LOGGER.error(e)

	train_items = open(opts.train).readlines()
	val_items = open(opts.val).readlines()

	copy_dataset(train_items,CONFIG,train=True)
	copy_dataset(val_items,CONFIG,train=False)


if __name__ == "__main__":
	
	optparser = optparse.OptionParser()
	optparser.add_option("-t", "--train", help="Training text", default="")
	optparser.add_option("-v", "--val", help="Validation text", default="")
	optparser.add_option("-c", "--config", help="Configuration file", default="")
	opts = optparser.parse_args()[0]

	main(opts)


