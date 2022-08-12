import video_maker
import image_scrapper
import data_scrapper_2
import time
from image_scrapper import folder_renewer


subjects = ['Abhimanyu','Adhiratha','Adrika','Agastya','Agni','Alambusha','Alayudha','Amba','Ambalika','Ambika','Ambika\'s maid','Amitaujas','Anjanaparvana','Aparajita','Arjuna','Aruni','Asoka','Ashvins','Ashwatthama','Ashtavakra','Astika','Avantini','Ayus','Ayodhaumya','Babruvahana','Babhru','Bahlika','Bakasura','Balarama','Bhadra','Madira','Bhagadatta','Bhanu','Bharadwaja','Bharata','Bhima','Bhima of Vidarbha','Bhishma','Bhrigu','Bhurishravas','Bhuri','Brihadbala','Brihadratha','Budha','Chandra','Chandravarma Kamboja','Gandharva King Chitrasena','Chekitana','Chitra','Chitrasena','Chitrāngada','Gandharva Chitrangada','Chitavahana','Chitravarma','Charudeshna','Damayanti','Dantavakra','Dasharaja','Dadhicha','Danda','Dandadhara','Darada','Devaki','Devasena','Dhrishtadyumna','Dhritrashtra','Dhrishtaketu of Chedi','Dhrishtaketu of Kekeya','Dirghaprajna','Draupadi','Drona','Drupada','Drumasena','Duryodhana','Duryodhana\'s wife(Bhanumati)','Dushala','Dushasana','Dushyanta','Durvasa','Eklavya','Gandhari','Gandhari\s maid','Ganesha','Ganga','Gada','Ghatotkacha','Hanuman','Hayagriva','Hamsa','Hidimba','Hidimbi','Ila','Indra','Iravan','Indradyumna','Jambavati','Janamejaya','Janapadi',
'Jarasandha','Jaratkaru','Jayadratha','Kadru','Kalyavana','Kacha','Kalki','Kamsa','Karna','Wives of Karna','Kaurava','Kichaka','Kirmira','Kripa','Kripacharya','Krishna','Kritavarma','Kunti','Laxman Kumara','Madri','Manasa','Markandeya','Menaka','Muchukunda','Nala','Nahusha','Nakula','Nanda Baba','Narakasura','Parashara','Parashuram','Parkshit','Pandu','Pradyumna','Pratipa','Pururavas','Rama','Revatu','Rohini','Rukmini','Rukmi','Sahadeva','Sahadeva of Magadha','Samba','Samvarana','Sanjaya','Sarama','Satrajit','Satyabhama','Satyaki','Satyavati','Savitri and Satyavan','Shakuni','Shakuntala','Shalya','Shantanu','Sharmishtha','Sarana','Shikhandi','Shishupala','Shukra','Subhadra','Sudakshina','Sudeshna','Surya','Susharma','Svaha','Takshaka','Tapati','Tilottama','Taraka','Usa','Ugrasena','Ugrashravas','Ulupi','Urvashi','Uttamaujas','Uttanka','Uttara','Uttarā',' Aniruddha ','Vaisampayana','Varaha','Vasudeva','Vayu','Vichitravirya','Vidura','Vikarna','Vinata','Virata','Vrihanta','Vrishasena','Vyasa','Yama','Yamuna','Yashoda','Yayati','Vindhyavasini','Yudhishthira','Yuyutsu']

ds_folder = 'Mahabharata'

folder_renewer(ds_folder)
for position in range(len(subjects)):
	try:
		subject = subjects.pop(0)+' Mahabharata'
		data_scrapper_2.data_scrapper(subject)
		image_scrapper.image_scrapper(subject)
		video_maker.video_maker(subject,destination_folder=ds_folder)
		
		
	except Exception as err:
		
		print(subject+f' caused an {err} error just skipping it````')
	time.sleep(10)
		

