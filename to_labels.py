import sys
def load_category_name(filepath):
	dat = open(filepath).readlines()
	mapping = {}
	with open("category_label.txt","wb") as f:
		for row in dat[1:]:
			cat_id, cat_name = row.strip().split("\t")
			f.write('_'.join(cat_name)+"\n")

load_category_name(sys.argv[1])
