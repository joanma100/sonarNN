import nn_utils as nnutil
import nn_sql_utils as sqlutil
import nn_soundcloud_utils as scutil

import os


# store the score given by a user to song
def set_Score(song_id, score, user=''):
	# store new score event
	sqlutil.save_score(song_id, score, user)

	# update song's score
	sqlutil.update_score_song(song_id, score)
	


# store a new song created by user (in midi format) or network
def store_song(song_id, generation = 0, user=''):
	# check song format and condition & save song into folder
	
	# store ID with score=0
	sqlutil.save_song(song_id, user, generation, 0)


# returns a list of wav songs to evaluate by users
def get_song_collection(song_folder):
	song_folder = os.getenv("HOME")+'/data/snr16/musica/dataset1/'
	return os.listdir(song_folder)


# publish media on SN
def publish(title, song_path):
	# upload WAV to soundcloud & tweet new song
	scutil.upload_soundcloud(title, song_path, gettoken())



# This function is in charge of selecting a set training set
# and train and store the resulting NN.
# Picks songs from the corresponding folder
def single_nn_job():

	# iterate for many different subsets of songs for training multiple NN
	network_id = 'something_nn3'	
	generation = sqlutil.check_generation()
	source_folder = 'generation_'+str(generation)
	file_hd5 = network_id+'_'+str(generation)+'_.hd5'

	# get_song_collection from natural selection
	training_set = get_song_collection(source_folder)

	# train	
	network = nnutil.train_network(training_set)

	# store training set information	
	sqlutil.save_training(network_id, training_set)

	# store network information
	sqlutil.save_nn(network_id, file_hd5)
	
	# generate new collection & store
	# update generation 
	sqlutil.update_generation(generation+1)
	# create folder
	generation = sqlutil.check_generation()
	destination_folder = 'generation_'+str(generation)
	new_collection = nnutil.generate_media(destination_folder)
	new_collection = training_set
	for song_id in new_collection:
		store_song(song_id, generation, network_id)
	# publish new media
	# publish(title, song_path)
	
	
def gettoken():
	return '00001'



