

import requests
from bs4 import BeautifulSoup
from url_downloader import save_file
import os


def folder_renewer(folder_name):
    '''Takes a folder name as arguement
    deletes everything from the folder
    And makes the folder if it already doesn't exist'''

    #Deletes The folder given with all items in it
    if os.path.exists(folder_name):

        items = os.listdir(folder_name)
        
        for item in items:
            os.remove('./'+folder_name+'/'+item)
        os.rmdir(folder_name)
    
    #Create the folder
    os.mkdir(folder_name)


def image_url_extractor(website_url,class_pattern,custom_src_predecessor='',custom_src_successor=''):
    '''Takes website url with subject in it,
Takes a class pattern of all <a>tags of images'''
    
    image_url_list = []

    #Soup Making
    try:
        response = requests.get(website_url)
        soup = BeautifulSoup(response.text,'html.parser')
    except Exception as err:
        print(err+' was raised')

    #Searching for img tags with pattern
    img_tag_list = soup.select(f'img.{class_pattern}')

    #Getting the src of <a> tags
    for img_tag in img_tag_list:
        img_url = custom_src_predecessor+img_tag.get('src')+custom_src_successor
        image_url_list.append(img_url)


    return image_url_list


def image_url_downloader(image_url_list,download_location='photos',img_format = '.png',image_limit=10):
    #Downloading everything from the image_url_list
    for img_position,urls in enumerate(image_url_list):

        #Keeping it short
        if img_position > image_limit:
            break

        save_file(url = urls,file_name=str(img_position)+img_format,file_path='./'+download_location)
        print('Downloaded image number: '+str(img_position+1))


def image_scrapper(subject,download_location = 'photos'):
    try:
        #Deletes the old photos and create a fresh new folder in the current path
        folder_renewer(download_location)
        
        subject = subject.replace(' ','+')
        
        #For now I'll use yandex only until later
        website_url = f'https://yandex.com/images/search?text={subject}'
        class_pattern='serp-item__thumb.justifier__thumb'

        image_url_list = image_url_extractor(website_url,class_pattern,custom_src_predecessor='https:')

        image_url_downloader(image_url_list,download_location)

        #Now with an extension for later making them into videos

    except Exception as err:
        print(err)
    

if __name__ == '__main__':
    subject = input('What?\n')
    image_scrapper(subject)
    print('Done!')
    
