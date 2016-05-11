import nn_utils as nnutil
import nn_sql_utils as sqlutil
import nn_soundcloud_utils as scutil

import os


# store the score given by a user to song
def set_Score(song_id, score, user=''):
	# store new score event
	sqlutil.sql_save_score(song_id, score, user):

	# update song's score
	sqlutil.sql_update_score(song_id, score_mod):
	


# store a new song created by user (in midi format) or network
def store_song(song, generation = 0, user=''):
	# check song format and condition & save song into folder
	
	# store ID with score=0
	sqlutil.sql_save_song(song, user, generation, 0):


# returns a list of wav songs to evaluate by users
def get_song_collection():
	for songs in os.listdir(getdirectory()):
		
		



# publish media on SN
def publish(title, song_path, token):
	# upload WAV to soundcloud & tweet new song
	scutil.upload_soundcloud(title, song_path, token)



# train again the network with a new training set
def batch_nn_job():
	# get_song_collection from natural selection
	training_set = get_song_collection()
	# train
	network = nnutil.train_network(training_set)
	# store training set information	
	sqlutil.sql_record_training(network, training_set)
	# store network information
	sqlutil.sql_record_nn(network, file_hd5)
	# generate new collection & store
	new_collection = nnutil.generate_media()
	for song in new_collection:
		store_song(song, user)
	# publish new media
	publish()
	


def getdirectory():
	# check directory of current generation in database
	return "gen_"+sqlutil.sql_check_generation()



