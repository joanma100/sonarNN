from .sonarNN import nn_sql_utils

# check song :

# song_id exists/not
nn_sql_utils.check_song(song_id)


# save song :
nn_sql_utils.save_song(song_id, creator, generation, score)


# updates song's score :
nn_sql_utils.update_score_song(song_id, score_mod)


# save score event
nn_sql_utils.save_score(song_id, score, user)


# we store information about each NN after training
nn_sql_utils.save_nn(nn_id, when, file_hd5)


# for each instance of the NN, we keep the songs on the training set
nn_sql_utils.save_training(nn_id, songs)	


# generation checks
nn_sql_utils.check_generation()
nn_sql_utils.update_generation(current_generation)


# SQL utils
nn_sql_utils.sql_create_tables()

nn_sql_utils.sql_delete_tables()


