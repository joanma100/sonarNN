import tinydb


db_path = 'db1.json'



# check if song is already on 'songs'
def check_song(song_id):
	
	db = tinydb.TinyDB( db_path )
	table1 = db.table('songs')
	songs = tinydb.Query()
	result = table1.search(songs.name==song_id)
	return result



# we store a song for each user creation OR neural network output
def save_song(song_id, parent, generation, score):
	db = tinydb.TinyDB( db_path )
	if (check_song(song_id)):
		print("Error: song already in DB")
		return None
	table1 = db.table('songs')
	now = 0
	table1.insert({'name': song_id, 'time': now, 'parent': parent, 'generation': generation, 'score': score})

	return 


# updates song's score in 'songs' table
def update_score_song(song_id, score_mod):
	return -1
	

# save score event in 'scores' table
def save_score(song_id, score, user):
	db = tinydb.TinyDB( db_path )
	table1 = db.table('scores')
	now = 0
	table1.insert({'name': song_id, 'score': score, 'time': now, 'user': user}) 
	return




# we store information about each NN after training
def save_nn(network_id, generation):
	db = tinydb.TinyDB( db_path )
	table1 = db.table('networks')
	now = 0
	table1.insert({'name':network_id, 'time': now, 'generation': generation})

	return




# for each instance of the NN, we keep the songs on the training set
def save_training(network_id, songs, generation):		
	db = tinydb.TinyDB( db_path )
	table1 = db.table('training')
	for song_id in songs:
		now = 0
		table1.insert({'network': network_id, 'song': song_id, 'time': now, 'generation': generation})

	return


def check_generation():	
	db = tinydb.TinyDB( db_path )
	table1 = db.table('generation')
	return table1.all()[0]['current']



def update_generation():
	db = tinydb.TinyDB( db_path )
	table1 = db.table('generation')
	current = check_generation()
	table1.purge()
	table1.insert({'current': current+1})
	return table1.all()[0]['current']



def create_tables():
	db = tinydb.TinyDB( db_path )
	# create 'songs'
	db.table('songs')
	# create 'scores'
	db.table('scores')
	# create 'networks'
	db.table('networks')
	# create 'training'
	db.table('training')
	# create 'generation'
	db.table('generation')



def delete_tables():
	db = tinydb.TinyDB( db_path )
	# delete 'songs'
	db.purge_table('songs')
	# delete 'scores'
	db.purge_table('scores')
	# delete 'networks'
	db.purge_table('networks')
	# delete 'training'
	db.purge_table('training')
	# delete 'generation'
	db.purge_table('generation')



