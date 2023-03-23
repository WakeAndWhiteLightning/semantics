import spacy

nlp = spacy.load('en_core_web_md')

tokens = nlp('person people flock crowd herd')
with open ('Semantics.txt', 'a+') as file:
    file.write('------------------MD OUTPUT------------------\n')
    for token1 in tokens:
        for token2 in tokens:
            result = (token1.text, token2.text, token1.similarity(token2))
            print(result)
            file.write(f'{str(result)}\n')
    file.write('''---------------------------------------------
    
    ''')

nlp = spacy.load('en_core_web_sm')

tokens = nlp('person people flock crowd herd')
with open ('Semantics.txt', 'a+') as file:
    file.write('------------------SM OUTPUT------------------\n')
    for token1 in tokens:
        for token2 in tokens:
            result = (token1.text, token2.text, token1.similarity(token2))
            print(result)
            file.write(f'{str(result)}\n')
    file.write('''---------------------------------------------
    
    ''')

#The smaller sm model throws a warnign when used in this way as there is no word vectors loaded. 
#The MD comes much closer to a similarity rating you would expect, e.g the singular 'person' has a much lower similarity with the group nouns 'flock, crowd, herd'
#Where the SM model gives a similar rating for people and flock as person and flock.


