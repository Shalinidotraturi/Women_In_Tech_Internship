Python 3.10.2 (tags/v3.10.2:a58ebcc, Jan 17 2022, 14:12:15) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
def add_prefix_un(word):
    return ('un'+word)

    
def make_word_groups(vocab_words):
        prefix=vocab_words[0]
        return((' :: '+prefix).join(vocab_words))
        
    

    


def remove_suffix_ness(word):
    index=word.find("ness")
    new_words=word[0:index]
    if(new_words[-1]=='i'):
        new_words=new_words[:-1]+"y"
    return new_words


def adjective_to_verb(sentence, index):
    k=sentence.split()
    word=k[index]
    if(word[-1]=='.'):
        word=word[:-1]
    return (word+'en')