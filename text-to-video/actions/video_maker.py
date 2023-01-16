from moviepy.editor import *

def video_maker(subject,image_source_folder_location='../cropped_photos',audio_source_folder_location='../speech/speach.mp3',destination_folder='media'):
    
    import os
    
    from tools.folder_renewer import folder_renewer



    folder_renewer(destination_folder,rm=False)


    photos = os.listdir(image_source_folder_location)
    for position , photo in enumerate(photos):
        photos[position] = './'+image_source_folder_location+'/'+photo


    audio_clip = AudioFileClip(audio_source_folder_location)
    
    

    duration = [5]#Duration of each images 

    for i in range(len(photos)):
        duration += duration
    
    image_clip = ImageSequenceClip(photos,durations=duration).set_duration(audio_clip.duration)


    main_clip = image_clip.set_audio(audio_clip)

    
    filename = './'+destination_folder+'/'+subject+'.mp4'
    
    main_clip.write_videofile(filename,fps=24)
