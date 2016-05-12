from  ..nn_server import *


# score songs 
song_id = 's0001'

set_Score(song_id, 2, user='')
set_Score(song_id, 1, user='')
set_Score(song_id, 3, user='')
set_Score(song_id, 1, user='')

song_id = 's0002'
store_song(song_id, 15, user='oioioi')


# get list of songs for next training
# get_song_collection()


# publish to soundcloud
# publish('checking upload', path, token)

# training of a single NN
single_nn_job()
