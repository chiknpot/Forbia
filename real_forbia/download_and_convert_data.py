'''
$ python download_and_convert_data.py \
    --dataset_name=imagedata \
    --dataset_dir=.

'''

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import tensorflow as tf

from datasets import download_and_convert_imagedata

FLAGS = tf.compat.v1.app.flags.FLAGS

tf.compat.v1.app.flags.DEFINE_string(
    'dataset_name',
    None,
    'The name of the dataset to convert, one of "data"'
    )

tf.compat.v1.app.flags.DEFINE_string(
    'dataset_dir',
    None,
    'The directory where the output TFRecords and temporary files are saved.')

tf.compat.v1.flags.DEFINE_float(
    'small_object_area_threshold', 0.005,
    'For --dataset_name=visualwakewords only. Threshold of fraction of image '
    'area below which small objects are filtered')

#tf.flags
tf.compat.v1.flags.DEFINE_string(
    'foreground_class_of_interest', 'person',
    'For --dataset_name=visualwakewords only. Build a binary classifier based '
    'on the presence or absence of this object in the image.')


def main(_):
  if not FLAGS.dataset_name:
    raise ValueError('You must supply the dataset name with --dataset_name')
  if not FLAGS.dataset_dir:
    raise ValueError('You must supply the dataset directory with --dataset_dir')

  if FLAGS.dataset_name == 'imagedata':
    download_and_convert_imagedata.run(FLAGS.dataset_dir)
  else:
    raise ValueError(
        'dataset_name [%s] was not recognized.' % FLAGS.dataset_name)

if __name__ == '__main__':
  tf.compat.v1.app.run()
