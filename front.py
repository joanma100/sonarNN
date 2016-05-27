import pygame
import time
import readchar

import nn_server


def hs(col_music):	
	freq = 44100    # audio CD quality
	bitsize = -16   # unsigned 16 bit
	channels = 2    # 1 is mono, 2 is stereo
	buffer = 1024    # number of samples
	pygame.mixer.init(freq, bitsize, channels, buffer)

	print music_file

	clock = pygame.time.Clock()
	
	for song in col_music:
		pygame.mixer.music.load(song)
		pygame.mixer.music.play()	
		while pygame.mixer.music.get_busy():
        		# check if playback has finished
			k = readchar.readchar()
			if k == 'h':
				print '+1'
				pygame.mixer.music.stop()
				break
			elif k == 's':
				print '-1'    
				pygame.mixer.music.stop()
				break
        		clock.tick(30)
		print 'next...'



def compose(path):
	nn.server
	
	
