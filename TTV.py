import video_maker
import image_scrapper
import data_scrapper_2
import image_scrapper_extenction
import os
import time


def TTV(subject):
	print('\r[-----] 0% Initializing the search......',end='',flush=True)
	subject = data_scrapper_2.data_scrapper(subject)
	#
	print(f'\r[█----] 20% DATA on the topic {subject} collected!',end='',flush=True)
	image_scrapper.image_scrapper(subject)
	#
	print(f'\r[██---] 40% Downloaded Images on the topic {subject}',end='',flush=True)
	image_scrapper_extenction.photo_cropper()

	print(f'\r[███--] 60% Cropped All previously downloaded Images...',end='',flush=True)
	video_maker.video_maker(subject)

	print(f'\r[████-] 80% Images and DATA combined to form a video!!',end='',flush=True)

	for path in ['photos','cropped_photos','speech']:
		image_scrapper.folder_renewer(path)
		os.rmdir(path)
	print(f'\r[█████] 100% Removed all cached files!Your video will be available in the TTV folder',end='\n',flush=True)



if __name__ == '__main__':
	subject = input('Please make sure the terms matches wikipedia page or it will raise errors\n')
	TTV(subject)


