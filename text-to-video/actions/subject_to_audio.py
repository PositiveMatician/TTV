import tools.data_handler as data_handlr
import tools.text_to_audio as audio_handlr
from tools.folder_renewer import folder_renewer
from tools.translate import translate




def subject_to_audio(subject,destination_folder = '../speech'):
    '''Takes a  subject[String] and saves a audio file.'''

    try:
        subject = data_handlr.subject_suggestor(subject)
        print('System Found the subject as '+subject)
        summary = data_handlr.summary_extractor(subject)
        print('Summary extracted ')
        summary = data_handlr.summary_filter(summary)
        print('Summary filtered and all the parenthesis have been removed')
        summary = translate(summary)
        print('Summary translated')
        folder_renewer(destination_folder)
        audio_handlr.text_to_audio(summary,location = destination_folder)
        print('Summary converted into audio')
        return subject
    except Exception as err:
        print(err)


        