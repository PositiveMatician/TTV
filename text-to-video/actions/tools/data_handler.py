#Univerasally needed modules
import wikipedia



'''
This file contains all functions related to string data which are the following
1.summary_extractor   -->(Subject to Summary)
2.subject_suggestor   -->(Subject filter)
3.summary_filter      -->(Summary filter)
'''

def summary_extractor(subject,max_sentences=4):
    '''Takes subject[String] and returns wikipedia summary[String]||||Parameters:max_sentences = No. of sentences which will be in summary(default = 4)'''
    

    try:
        summary = wikipedia.summary(subject,sentences=max_sentences)
        #Number of sentences determines the length of summary
        return summary

    except Exception as err:
        print(f'The requested search on topic: {subject} was not found or caused {err}, please try something else')


def subject_suggestor(subject):
    '''Takes a subject[String] and returns the most likely related topic from wikipedia'''

    while wikipedia.suggest(subject):
        subject = wikipedia.suggest(subject)

    return subject


def summary_filter(summary_text):
    '''Takes a String as arguement and returns a string without any parenthesis,newlines and double spaces
		Note:- While removing parenthesis it also removes the info between the parenthesis 
		'''
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


if __name__=='__main__':
    subject = input('Subject?\n')
    print(1)
    subject = subject_suggestor(subject)
    print(2)
    summary = summary_extractor(subject)
    print(3)
    summary = summary_filter(summary)
    print(summary)