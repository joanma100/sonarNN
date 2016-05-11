import nn_utils as nnu
import nn_sql_utils as sqlu
import nn_soundcloud_utils as scu

import os


# store the score given by a user to song
def set_Score(song, score):
	# store new score
	
	


# store a song created by user (in midi format)
def store_song(song, user):
	# check song format and condition
	# save song into folder
	# create song ID
	# store ID and score



# returns a list of wav songs to evaluate by users
def get_song_collection():
	for songs in os.listdir(MUSIC_DIRECTORY):
		
		



# publish media on SN
def publish():
	# upload WAV to soundcloud & tweet new song
	scu.upload_soundcloud(title, song_path, token)



# train again the network with a new training set
def batch_work():
	# get_song_collection from natural selection
	training_set = get_song_collection()
	# train
	network = nnu.train_network(training_set)
	# store training set information	
	sqlu.sql_record_training(network, training_set)
	# store network information
	when = date()
	sqlu.sql_record_nn(network, when, file_hd5)
	# generate new collection & store
	new_collection = nnu.generate_media()
	for song in new_collection:
		store_song(song, user)
	# publish new media
	publish()
	














