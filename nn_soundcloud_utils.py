import soundcloud



def upload_soundcloud():
	client = soundcloud.Client(client_id=YOUR_CLIENT_ID,
	                           client_secret=YOUR_CLIENT_SECRET,
	                           redirect_uri="http://your/redirect/uri")
	
	
