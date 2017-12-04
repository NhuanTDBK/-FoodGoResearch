# FoodGoResearch

-  FoodGoResearch: Python2.7
-  Preprocessing: 
	- "python preprocessing/export_to_xml.py config.yml"
  - "python create_label_pbtxt.py --filepath UECFOOD256/category.txt --output_path map.pbtxt"
 - Create train/val text: 
 - Split train/val dataset:
      python datasets/split_dataset.py --train uecfood256_split/train.txt --val uecfood256_split/val.txt --config config.yml
 - Create config_train and config_val.yml
 - python datasets/create_google_structure.py --config config_train.yml --file_name train.tfrecord
 - python datasets/create_google_structure.py --config config_val.yml --file_name val.tfrecord
 
 
	
