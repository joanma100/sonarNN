import soundcloud


def upload_soundcloud(title, song_path, token):
	# create a client object with access token
	client = soundcloud.Client(access_token=token)
	# upload audio file
	track = client.post('/tracks', track={
	    'title': title,
	    'asset_data': open(song_path, 'rb')
	})
	# link twitter account here




