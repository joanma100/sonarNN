from  ..nn_sql_utils import *

# SQL utils
delete_tables()
create_tables()


# save song :

song_id = 's0001'
creator = 'me me'
generation = 0
score = 0

save_song(song_id, creator, generation, score)

# check song :

# song_id exists/not
print check_song(song_id)[0][0]


# updates song's score :
score_mod = 1
update_score_song(song_id, score_mod)
print check_song(song_id)

# save score event
save_score(song_id, score, creator)


# we store information about each NN after training
network_id = 'n0001'
file_hd5 = network_id+'.hd5'
save_nn(network_id, file_hd5)


# for each instance of the NN, we keep the songs on the training set
songs = [song_id, 's0002', 's0003']

save_training(network_id, songs)	


# generation checks
current_generation = 1
update_generation(current_generation)
next = check_generation()
next = next+1
update_generation(next)
print check_generation()
current_generation = 3
update_generation(current_generation)
print check_generation()


