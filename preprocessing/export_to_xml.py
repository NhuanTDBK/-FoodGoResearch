import xml.etree.ElementTree as ET
from PIL import Image
from copy import deepcopy
import os
import optparse
import logging
import yaml
import sys

logging.basicConfig(level=logging.INFO)
LOGGER = logging.getLogger(__name__)

CONFIG = yaml.load(open(sys.argv[1]))

ANNOTATION_FOLDER = CONFIG["ANNOTATION_FOLDER"]
DATA_FOLDER = CONFIG["DATA_FOLDER"]
N_LABELS = CONFIG["N_LABELS"]

sample_xml = ET.parse("sample.xml")


def get_width_height(filepath):
	with Image.open(filepath) as img:
		width, height = img.size
		return width,height

def create_object_element(element, name="",xmin=0,ymin=0,xmax=0,ymax=0):
	name_element = ET.SubElement(element,"name")
	name_element.text = name
	
	truncated_element = ET.SubElement(element,"truncated")
	truncated_element.text = "0"
	
	difficult_element = ET.SubElement(element,"difficult")
	difficult_element.text = "0"
	
	bndbox_element = ET.SubElement(element,"bndbox")

	xmin_element = ET.SubElement(bndbox_element,"xmin")
	xmin_element.text = xmin
	ymin_element = ET.SubElement(bndbox_element,"ymin")
	ymin_element.text = ymin
	xmax_element = ET.SubElement(bndbox_element,"xmax")
	xmax_element.text = xmax
	ymax_element = ET.SubElement(bndbox_element,"ymax")
	ymax_element.text = ymax			

	return element

def load_category_name(filepath):
	dat = open(filepath).readlines()
	mapping = {}
	for row in dat[1:]:
		cat_id, cat_name = row.strip().split("\t")
		print(cat_id,cat_name)
		mapping[int(cat_id)] = '_'.join(cat_name.split(" "))
	return mapping

def iterate_label_folder(folder_name,label):
	bb_info_f = open(os.path.join(folder_name,"bb_info.txt"))
	dat = bb_info_f.readlines()
	for row in dat[1:]:
		name, xmin,ymin,xmax,ymax = row.strip().split(' ')
		filepath = folder_name + "/" + name+'.jpg'
		filepath_xml = os.path.join(ANNOTATION_FOLDER,name+'.xml')
		LOGGER.info(filepath)

		if os.path.exists(filepath):
			
			if not(os.path.exists(filepath_xml)):

				sample_format_xml = deepcopy(sample_xml)
				root = sample_format_xml.getroot()

				width,height = get_width_height(filepath)
				folder_name_element = root.getiterator("folder")[0]
				folder_name_element.text = DATA_FOLDER
				filename_element = root.getiterator("filename")[0]
				filename_element.text = name+".jpg"
				width_element = root.getiterator("width")[0]
				width_element.text = str(width)
				height_element = root.getiterator("height")[0]
				height_element.text = str(height)

				object_element = ET.SubElement(root,"object")
				object_element_filled = create_object_element(object_element,
					label,
					xmin,ymin,xmax,ymax)

				sample_format_xml.write(filepath_xml)
			else:
				LOGGER.info("Existing")
				sample_format_xml = ET.parse(filepath_xml)
				root = sample_format_xml.getroot()
				object_element = ET.SubElement(root,"object")
				object_element_filled = create_object_element(object_element,
					label,
					xmin,ymin,xmax,ymax)
				sample_format_xml.write(filepath_xml)

def main():
	try:
		os.mkdir(ANNOTATION_FOLDER)
	except:
		print("Folder existed")
	mapping_idx_to_name = load_category_name("{ROOT}/category.txt".format(ROOT=DATA_FOLDER))
	for idx in range(1,N_LABELS+1):
		iterate_label_folder("{ROOT}/{INDEX}".format(ROOT=DATA_FOLDER,INDEX=idx),mapping_idx_to_name[idx])


if __name__ == "__main__":

	main()
