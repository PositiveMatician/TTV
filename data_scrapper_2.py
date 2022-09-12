
import wikipedia



def subject_suggestor(subject):
    while wikipedia.suggest(subject):
        subject = wikipedia.suggest(subject)
    return subject


def summary_extractor(subject,max_sentences=4):
    try:
        summary = wikipedia.summary(subject,sentences=max_sentences)
        #Number of sentences determines the length of summary
        return summary
    except Exception as err:

        print(f'The requested search on topic: {subject} was not found or caused {err}, please try something else')

    
def summary_filter(summary_text):
    #Summary had to be filtered or else while converting it into speech some uncommon sounding things can be heard 
    if '(' in summary_text:
        
        for some_number in range(summary_text.count('(')):#Did considered Re for this but couldn't get it to work
            open_bracket_position = summary_text.index('(')
            close_bracket_positon = summary_text.index(')')
            
            predeccesor = summary_text[0:open_bracket_position]
            successor = summary_text[close_bracket_positon+1:]
            if open_bracket_position > close_bracket_positon:
                close_bracket_positon = summary_text.index(')')
                
                predeccesor = summary_text[0:close_bracket_positon]
                successor = summary_text[close_bracket_positon+1:]
                summary_text = predeccesor+successor
                continue
            summary_text = predeccesor+successor
        #This Programm Stores all the text before the first open bracket and all text after first closed bracket
        #To get errors just put Parenthesis(curved brackets) inside another Parenthesis
    if ')' in summary_text:
        #This Trys to eliminate any lonly closed brackets before open ones
            for some_number in range(summary_text.count(')')):
                close_bracket_positon = summary_text.index(')')
                
                predeccesor = summary_text[0:close_bracket_positon]
                successor = summary_text[close_bracket_positon+1:]
                summary_text = predeccesor+successor
    summary_text.replace('  ',' ').replace('\n','')#This tries to remove any double spaces and minimize the summary in one parah
    return summary_text


def text_to_audio(text):
    from image_scrapper import folder_renewer
    from translate import translate
    from gtts import gTTS


    folder_renewer('speech')
    text = summary_filter(text)
    text = translate(text)
    text_to_speech = gTTS(text,tld='co.in',lang='hi')
    text_to_speech.save('./speech/speech.mp3')   
    

def data_scrapper(subject):
    try:
        subject = subject_suggestor(subject)
        summary = summary_extractor(subject)
        text_to_audio(summary)
        return subject
    except Exception as err:
        print(err)


if __name__ == '__main__':
    subject = input('What?\n')
    print(data_scrapper(subject))