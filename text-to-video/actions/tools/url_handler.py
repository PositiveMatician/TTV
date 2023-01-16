'''
Handles downloading images from internet
1.image_url_extractor
2.image_url_downloader
'''





def image_url_extractor(website_url,class_pattern,custom_src_predecessor='',custom_src_successor=''):
    '''Takes website url with subject in it,
Takes a class pattern of all <a>tags of images and return a list of urls'''
    from bs4 import BeautifulSoup
    import requests

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
	'''Takes a list of url and downloads them'''
	from url_downloader import save_file
    
	#Downloading everything from the image_url_list
	for img_position,urls in enumerate(image_url_list):

        #Keeping it short
		if img_position > image_limit:
			break

		save_file(url = urls,file_name=str(img_position)+img_format,file_path='./'+download_location)
        
