from image_scrapper import folder_renewer
import wikipedia
from gtts import gTTS
import os

def summary_extractor(subject,max_sentences=4):

    if wikipedia.search(subject):

        if type(wikipedia.search(subject))==str():
            #Replaces the subject with top search results of the topic to prevent any PageNotFOund Error
            subject=wikipedia.search(subject)

        elif type(wikipedia.search(subject))==list():
            subject= wikipedia.search(subject)[0]

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


def data_scrapper(subject,summary = None):
    try:
        folder_renewer('speech')
        if summary == None:
            summary = summary_extractor(subject)

        summary = summary_filter(summary)

        text_to_speech = gTTS(summary,tld='co.in',lang='hi')
        text_to_speech.save('./speech/speech.mp3')
        
        print('Installed a audio version!')

        return summary
    except Exception as err:
        print(err)


if __name__ == '__main__':
    subject = input('What?\n')
    print(data_scrapper(subject))