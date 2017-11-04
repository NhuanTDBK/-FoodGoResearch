from darkflow.net.build import TFNet
import cv2
import optparse

if __name__ == "__main__":
	optparser = optparse.OptionParser()
	optparser.add_option("-p", "--pbLoad", help="pb load", default="")
	optparser.add_option("-m", "--metaLoad", help="meta load", default="")
	optparser.add_option("-t", "--threshold", help="meta load", default=0.1)
	optparser.add_option("-i", "--image", help="meta load", default="")	
	opts = optparser.parse_args()[0]

	options = {"pbLoad": opts.pbLoad,"metaLoad":opts.metaLoad, "threshold": 0.0}
	tfnet = TFNet(options)
	imgcv = cv2.imread(opts.image)
	result = tfnet.return_predict(imgcv)
	print(result)