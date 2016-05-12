import sys, os

sys.path.insert(0, os.getenv("HOME")+"/data/snr16/")
import biaxial as bx
from biaxial import multi_training, model

## single NN main functions


# training routine
def train_network(training_set):
	# convert midi to input dataset
	# train
	print 'NN start training'
	pcs = multi_training.loadPieces(os.getenv("HOME")+"/data/snr16/biaxial/music")
	m = model.Model([100,100],[100,50], dropout=0.5)
	multi_training.trainPiece(m, pcs, 10000)


# generation routine from the trained network
def generate_media(destination_folder):
	# generates songs % stores new files in folder
	print 'NN start generation'
	
