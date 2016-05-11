import mysql.connector
from datetime import date


# helper: sanity check if song is already there
def check_song(song_id):
	cnx = sql_connect()
	cursor = cnx.cursor()
	check_song = "SELECT * FROM songs WHERE name = '%s'" % song_id
	try:	
		cursor.execute(check_song)
		results = cursor.fetchall()
		if results:	
			cursor.close()
			cnx.close()
			return 1	
	except:
		print "Error: unable to find song"	
		cursor.close()
		cnx.close()
		return None



# we store a song for each user creation OR neural network output
def save_song(song_id, creator, generation, score):
	if (sql_check_song(song_id)):
		print "Error: song already in DB"
		return None

	cnx = sql_connect()
	cursor = cnx.cursor()

	add_song = ("INSERT INTO songs "
               "(name, time, creator, generation, score) "
               "VALUES (%s, now(), %s, %s, %s)")

	cursor.execute(add_song, (song_id, creator, generation, score))
	cnx.commit()
	
	cursor.close()
	cnx.close()
	return 1


# updates song's score in 'songs' table
def update_score_song(song_id, score_mod):
	if (sql_check_song(song_id)):
		cnx = sql_connect()
		cursor = cnx.cursor()

		update_song = "UPDATE songs SET score = score + %d WHERE name = '%s'" % (score_mod, song_id)

		cnx.commit()
		cursor.close()
		cnx.close()
		return 1
	else:
		print "Error: song not found, unable to score"


# only users score a song HIT<=>SHIT
def save_score(song_id, score, user):
	cnx = sql_connect()
	cursor = cnx.cursor()

	add_score = "INSERT INTO scores (time, song, score, user) VALUES (now(), %s, %s, %s)" % (song_id, score, user)

	cursor.execute(add_score)
	cnx.commit()
	cursor.close()
	cnx.close()
	return




# we store information about each NN after training
def save_nn(nn_id, when, file_hd5):
	cnx = sql_connect()
	cursor = cnx.cursor()

	add_nn = ("INSERT INTO networks "
               "(name, when, file_hd5) "
               "VALUES (%s, now(), %s)")

	cursor.execute(add_nn, (nn_id, file_hd5))
	cnx.commit()
	cursor.close()
	cnx.close()
	return




# for each instance of the NN, we keep the songs on the training set
def save_training(nn_id, songs):	
	cnx = sql_connect()
	cursor = cnx.cursor()

	add_training = ("INSERT INTO training (network, song) VALUES (%s, %s)" % (nn_id, song)

	for song in songs:
		cursor.execute(add_training)

	cnx.commit()
	cursor.close()
	cnx.close()
	return



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



def sql_create_tables():

	# create 'songs'
	
	# create 'scores'

	# create 'networks'

	# create 'training'

	# create 'generation'


def sql_delete_tables():
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


def check_generation():
	cnx = sql_connect()
	cursor = cnx.cursor()
	check_generation = "SELECT * FROM generation"
	cursor.execute(check_generation)	
	cnx.commit()
	cursor.close()
	cnx.close()
	return cursor.fetchall()



def update_generation(current_generation):
	cnx = sql_connect()
	cursor = cnx.cursor()
	update_generation = "UPDATE generation SET current = '%s'" % current_generation
	cursor.execute(update_generation)	
	cnx.commit()
	cursor.close()
	cnx.close()


# sql_check_song('df')
# sql_record_song('df5',001,0,0)

