import time

generations = 4 
hs_robots = 10
comp_robots = 10
delay = 5

def client_process():
	for _ in range(generations):
		songs = range(5); #	get_song_collection(song_folder)
		# launch h/s robots:
		for s in songs:
			random_vote(s)
		# launch composer robot:
		for _ in range(comp_robots):
			random_composition()
		time.sleep(delay)
	

def random_vote(song):
	# submit h/s vote
	print('Submit score')	
	#set_Score(song_id, score, user='')
	return


def random_composition():
	# submit song file
	print('Submit song')
	#store_song(song_id, generation = 0, user='')
	return



if __name__ == "__main__":
	client_process()	

