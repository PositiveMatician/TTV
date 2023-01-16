
import subject_to_audio 
import subject_to_png
import video_maker
import time 




keyword = ''+''
subjects = ['Rafael Nadal']

for position,subject in enumerate(subjects):
	# subject = subject + keyword
	try:
		print('Process started on '+subject)
		subject = subject_to_audio.subject_to_audio(subject)
		print('Audio extracted')
		print(subject,'\n',f'{position}/{len(subjects)}')
		dl = subject_to_png.subject_to_png(subject)
		print('Image extracted')
		video_maker.video_maker(subject=subject,image_source_folder_location=dl)
		print('Done')
	except Exception as err:
		print(err)
	time.sleep(25)


	
