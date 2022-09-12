

def translate(text):
    from googletrans import Translator

    return Translator().translate(text, dest = 'hi').text




if __name__=='__main__':
    print(translate(text))