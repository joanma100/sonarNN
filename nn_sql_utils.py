import mysql.connector
from datetime import date


# check if song is already on 'songs'
def check_song(song_id):
	cnx = sql_connect()
	cursor = cnx.cursor()
	check_song = "SELECT * FROM songs WHERE song_id = '%s'" % song_id
	try:	
		cursor.execute(check_song)
		results = cursor.fetchall()
		if results:	
			cursor.close()
			cnx.close()
			return results	
	except:
		print "Error: unable to find song"	
		cursor.close()
		cnx.close()
		return None



# we store a song for each user creation OR neural network output
def save_song(song_id, creator, generation, score):
	if (check_song(song_id)):
		print "Error: song already in DB"
		return None

	cnx = sql_connect()
	cursor = cnx.cursor()

	add_song = "INSERT INTO songs (song_id, time, creator, generation, score)\
			VALUES ('%s', now(), '%s', %s, %s)" %(song_id, creator, generation, score)

	cursor.execute(add_song)
	cnx.commit()
	
	cursor.close()
	cnx.close()
	return 1


# updates song's score in 'songs' table
def update_score_song(song_id, score_mod):
	if (check_song(song_id)):
		cnx = sql_connect()
		cursor = cnx.cursor()

		update_song = "UPDATE songs SET score = score + %d WHERE song_id = '%s'" % (score_mod, song_id)
		
		cursor.execute(update_song)
		cnx.commit()
		cursor.close()
		cnx.close()
		return 1
	else:
		print "Error: song not found, unable to score"


# save score event in 'scores' table
def save_score(song_id, score, user):
	cnx = sql_connect()
	cursor = cnx.cursor()

	add_score = "INSERT INTO scores (song_id, score, time, creator) VALUES ('%s', %d, now(), '%s')" % (song_id, score, user)

	cursor.execute(add_score)
	cnx.commit()
	cursor.close()
	cnx.close()
	return




# we store information about each NN after training
def save_nn(network_id, file_hd5):
	cnx = sql_connect()
	cursor = cnx.cursor()

	add_nn = "INSERT INTO networks (network_id, time, path) VALUES ('%s', now(), '%s')" % (network_id, file_hd5)

	cursor.execute(add_nn)
	cnx.commit()
	cursor.close()
	cnx.close()
	return




# for each instance of the NN, we keep the songs on the training set
def save_training(network_id, songs):	
	cnx = sql_connect()
	cursor = cnx.cursor()

	for song in songs:
		add_training = "INSERT INTO training (network_id, time, song_id) VALUES ('%s', now(), '%s')" % (network_id, song)
		cursor.execute(add_training)

	cnx.commit()
	cursor.close()
	cnx.close()
	return


def check_generation():
	cnx = sql_connect()
	cursor = cnx.cursor()
	check_generation = "SELECT * FROM generation"
	cursor.execute(check_generation)	
	result = cursor.fetchall()
	cnx.commit()
	cursor.close()
	cnx.close()
	return result[0][0]



def update_generation(current_generation):
	cnx = sql_connect()
	cursor = cnx.cursor()
	update_generation = "UPDATE generation SET generation_id = %d" % current_generation
	cursor.execute(update_generation)	
	cnx.commit()
	cursor.close()
	cnx.close()





def sql_connect():
	cnx = mysql.connector.connect(user='root',password='',host='127.0.0.1',database='snr16_test')
	return cnx


def sql_simple_query(query):
	cnx = sql_connect()
	cursor = cnx.cursor()
	cursor.execute(query)
	cnx.commit()
	cursor.close()
	cnx.close()



def create_tables():
	cnx = sql_connect()
	cursor = cnx.cursor()

	# create 'songs'
	cursor.execute("CREATE TABLE songs (song_id varchar(20), time DATETIME, creator varchar(20), \
			generation INTEGER, score REAL, PRIMARY KEY(song_id))")
	# create 'scores'
	cursor.execute("CREATE TABLE scores (song_id varchar(20), score REAL, \
			time DATETIME, creator varchar(20))")
	# create 'networks'
	cursor.execute("CREATE TABLE networks (network_id varchar(20), \
			time DATETIME, path varchar(20), PRIMARY KEY(network_id) )")
	# create 'training'
	cursor.execute("CREATE TABLE training (network_id varchar(20), \
			time DATETIME, song_id varchar(20))")
	# create 'generation'
	cursor.execute("CREATE TABLE generation (generation_id INTEGER)")
	cursor.execute("INSERT INTO generation (generation_id) VALUE (0)")
	cnx.commit()
	cursor.close()
	cnx.close()



def delete_tables():
	cnx = sql_connect()
	cursor = cnx.cursor()

	# delete 'songs'
	cursor.execute("DROP TABLE songs")
	# delete 'scores'
	cursor.execute("DROP TABLE scores")
	# delete 'networks'
	cursor.execute("DROP TABLE networks")
	# delete 'training'
	cursor.execute("DROP TABLE training")
	# delete 'generation'
	cursor.execute("DROP TABLE generation")

	cnx.commit()
	cursor.close()
	cnx.close()



