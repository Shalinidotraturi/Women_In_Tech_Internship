Python 3.5.1 (v3.5.1:37a07cee5969, Dec  6 2015, 01:54:25) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def capitalize_title(title):
    return title.title()
    

def check_sentence_ending(sentence):
    flag=False
    if sentence[-1]=='.':
        flag=True

    return flag


def clean_up_spacing(sentence):
    return sentence.strip()
    
def replace_word_choice(sentence, old_word, new_word):
    return sentence.replace(old_word,new_word)
    
