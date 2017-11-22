import logging
import os
import json
from lxml import etree
import tensorflow as tf

flags = tf.app.flags
flags.DEFINE_string('filepath', '', 'File category')
flags.DEFINE_string('data_dir', '', 'Root directory to raw PASCAL VOC dataset.')
flags.DEFINE_string('output_path', '', 'Path to output TFRecord')
flags.DEFINE_string('label_map_path', 'data/pascal_label_map.pbtxt',
                    'Path to label map proto')

FLAGS = flags.FLAGS

def load_category_name(filepath,tf_writer):

  dat = open(filepath).readlines()
  cat = {}
  # item_list = string_int_label_map_pb2.StringIntLabelMap()
  for row in dat[1:]:
    cat_id, cat_name = row.strip().split("\t")
    cat_id = int(cat_id)
    name = '_'.join(cat_name.split(" "))
    cat[name] = cat_id

  writer.write(json.dumps(cat))
  writer.close()

if __name__=="__main__":

  writer = open(FLAGS.output_path,"wb")
  load_category_name(FLAGS.filepath,writer)
