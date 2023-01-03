#This program reads a file of movie descriptions and returns the movie the user should watch next
#based on their previously watched movie

import spacy
nlp = spacy.load('en_core_web_md')
movie_file = open('movies.txt','r')

def next_movie(description):
    #the example movie description is cast into a doc object for nlp methods to word
    results = []
    description = nlp(description)
    #for each line in the movie file the description is compared to the example description
    for line in movie_file:
        current_movie = line.split(":")
        current_title = current_movie[0]
        current_movie_d = current_movie[1]
        #this splits the line into the title of the movie and its description
        current_movie_d = nlp(current_movie_d)
        result = current_movie_d.similarity(description)
        #each result appended to a nested list containing each of the results
        results.append([current_title,current_movie_d,result])
    '''Because the results are a list of lists and we know which entry will be the similarity number
    the key for our lambda is the 3rd entry for each list in our nested list.
    SO the max value is calculated only from these entries
    returning the most similar film to the one the user provided (or the example as used here)'''
    next_to_watch = max(results, key=lambda x: x[2])
    #this then only returns the title of the movie, not its description or similarty number
    next_to_watch_title = next_to_watch[0]
    return(next_to_watch_title)

#this is where the user could enter their own movie and its description
movie_title = "Planet Hulk"
movie_description = '''Will he save
their world or destroy it? When the Hulk becomes too dangerous for the
Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a
planet where the Hulk can live in peace. Unfortunately, Hulk land on the
planet Sakaar where he is sold into slavery and trained as a gladiator.'''
#here planet hulk is the example used to be passed into the function above
result = next_movie(movie_description)
print(f"After watching {movie_title}, The next movie you should watch is {result}")
movie_file.close()