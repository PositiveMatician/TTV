
import tools.url_handler as url_handlr
from tools.folder_renewer import folder_renewer
from tools.image_handler import photo_cropper


def subject_to_png(subject,download_location = '../photos'):
    try:
        #Deletes the old photos and create a fresh new folder in the current path
        folder_renewer(download_location)
        
        subject = subject.replace(' ','+')
        
        #For now I'll use yandex only until later
        website_url = f'https://yandex.com/images/search?text={subject}'
        class_pattern='serp-item__thumb.justifier__thumb'

        image_url_list = url_handlr.image_url_extractor(website_url,class_pattern,custom_src_predecessor='https:')

        url_handlr.image_url_downloader(image_url_list,download_location)
        print('Images downloaded')

        #Cropping the images
        folder_renewer(download_location+'(cropped)')
        photo_cropper(folder_name=download_location,destination_folder = download_location+'(cropped)' )
        print('Images cropped')
        return download_location+'(cropped)'

    except Exception as err:
        print(err)
    

