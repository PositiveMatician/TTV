from PIL import Image
import os
import image_scrapper


#Photo cropping
#This is needed to use moviepy on the images 
def photo_cropper(folder_name='photos',image_limit=10):
    #
    photos_list = os.listdir(folder_name)
    #
    for position,photo in enumerate(photos_list):
        photos_list[position] = './'+folder_name+'/'+photo
    #
    #Remake the folder every time
    image_scrapper.folder_renewer('cropped_photos')

    
    #bg.jpg is the dimension place holder it determines what will be the dimensions of all the cropped images
    with Image.open('bg.jpg') as bg:
        for number,photos in enumerate(photos_list):
            #
            if number > image_limit :
                break#The amount is reduced to 10, as it was the limit of my computer to handle, while using moviepy
            #
            with Image.open(photos) as photo:
                
                photo = photo.resize(size=bg.size,) 
                
                photo.save(photos.replace('./'+folder_name+'/','./'+'cropped_photos'+'/'))
            
    

if __name__ == '__main__':
    photo_cropper()
    print('Done!')


