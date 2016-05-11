from sonarNN import nn_server as serv
import os



def test_suite_HS():
	
	# get song collection
	setlist = serv.get_song_collection()

	# loop over collection, collect votes and store them
	for song in setlist:
		score = HS(song)
		serv.set_Score(song, score)
		
		


def test_suite_compose():

	# generate_songs
	path, generate_song()

	# store songs in folder

	# store song's information
	serv.store_song(song, user)




# local defs
def HS(song):
	return 1
	

def generate_song():
	path = os.getenv("HOME")+"/music"
	song_id	= '00001'
	return song_id, path







