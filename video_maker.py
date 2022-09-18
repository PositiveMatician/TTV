

import os
from moviepy.editor import *
from image_scrapper import folder_renewer



def video_maker(subject,source_folder_location='cropped_photos',destination_folder='TTV'):
    folder_renewer(destination_folder)


    photos = os.listdir(source_folder_location)
    for position , photo in enumerate(photos):
        photos[position] = './'+source_folder_location+'/'+photo


    audio_clip = AudioFileClip('./speech/speech.mp3')
    
    

    duration = [5]#Duration of each images 

    for i in range(len(photos)):
        duration += duration
    
    image_clip = ImageSequenceClip(photos,durations=duration).set_duration(audio_clip.duration)


    main_clip = image_clip.set_audio(audio_clip)

    
    filename = './'+destination_folder+'/'+subject+'.mp4'
    
    main_clip.write_videofile(filename,fps=24,logger=None)




if __name__ == '__main__':
    
    video_maker('test')
    print('Done!')


