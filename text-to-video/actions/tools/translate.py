
def translate(text,lang = 'hi'):
    '''Uses google translate to translate text'''
    from googletrans import Translator

    return Translator().translate(text, dest = lang).text


