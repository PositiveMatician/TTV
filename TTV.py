import video_maker
import image_scrapper
import data_scrapper_2
import image_scrapper_extenction

def TTV(subject):

	data_scrapper_2.data_scrapper(subject)
	image_scrapper.image_scrapper(subject)

	image_scrapper_extenction.photo_cropper()
	#
	video_maker.video_maker(subject)



if __name__ == '__main__':
	subject = input('Please make sure the terms matches wikipedia page or it will raise errors\n')
	TTV(subject)


