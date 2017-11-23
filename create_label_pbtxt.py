import hashlib
import io
import logging
import os

from lxml import etree
import PIL.Image
import tensorflow as tf

flags = tf.app.flags
flags.DEFINE_string('filepath', '', 'File category')
flags.DEFINE_string('output_path', '', 'Path to output TFRecord')

templates = lambda id, name: """
item {
    name: "%s"
    id: %s
}"""%(name,id)

FLAGS = flags.FLAGS

def load_category_name(filepath,tf_writer):

  dat = open(filepath).readlines()
  for row in dat[1:]:
    cat_id, cat_name = row.strip().split("\t")
    id = int(cat_id)
    name = '_'.join(cat_name.split(" "))
    writer.write(templates(id,name))
  writer.write("\n")
  writer.close()

if __name__=="__main__":

  writer = open(FLAGS.output_path,"wb")
  load_category_name(FLAGS.filepath,writer)
