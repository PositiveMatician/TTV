


def text_to_audio(text,location = 'speach'):
    '''Takes text as arguements and saves a audio file in the given location'''

    from gtts import gTTS
    text_to_speech = gTTS(text,tld='co.in',lang='hi')
    text_to_speech.save(location+'/speach.mp3')   
    