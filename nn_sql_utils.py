import mysql.connector
from datetime import date



# we store a song for each user creation OR neural network output
def record_song(name, when, creator, generation, score):
	cnx = mysql.connector.connect(user='root', password='',
                              host='127.0.0.1',
                              database='snr16_test')

	cursor = cnx.cursor()
	add_song = ("INSERT INTO songs "
               "(name, time, creator, generation, score) "
               "VALUES (%s, %s, %s, %s, %s)")

	cursor.execute(add_song, (name, when, creator, generation, score))
	cnx.commit()
	cursor.close()
	cnx.close()
	return



# only users score a song HIT<=>SHIT
def record_score(when, song_id, score, user):
	cnx = mysql.connector.connect(user='root', password='',
                              host='127.0.0.1',
                              database='snr16_test')

	cursor = cnx.cursor()
	add_score = ("INSERT INTO songs "
               "(time, song, score, user) "
               "VALUES (%s, %s, %s, %s)")

	cursor.execute(add_score, (when, song_id, score, user))
	cnx.commit()
	cursor.close()
	cnx.close()
	return


# we store information about each NN after training
def record_nn(network, when, file_hd5):
	cnx = mysql.connector.connect(user='root', password='',
                              host='127.0.0.1',
                              database='snr16_test')

	cursor = cnx.cursor()
	add_nn = ("INSERT INTO nn "
               "(name, when, file_hd5) "
               "VALUES (%s, %s, %s)")

	cursor.execute(add_nn, (network, when, file_hd5))
	cnx.commit()
	cursor.close()
	cnx.close()
	return


# for each instance of the NN, we keep the songs on the training set
def record_training(network, songs):	
	cnx = mysql.connector.connect(user='root', password='',
                              host='127.0.0.1',
                              database='snr16_test')
	
	cursor = cnx.cursor()
	add_training = ("INSERT INTO nn "
               "(network, song) "
               "VALUES (%s, %s)")
	for song in songs:
		cursor.execute(add_training, (network, song))

	cnx.commit()
	cursor.close()
	cnx.close()
	return



record_song('df2',date(2016,05,02),001,0,0)
