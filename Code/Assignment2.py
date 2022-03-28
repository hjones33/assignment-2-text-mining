# The code I ran through the command prompt
# pip install pymediawiki
# pip install nltk
# pip install thefuzz
# import nltk
# nltk.download('vader_lexicon')

from mediawiki import MediaWiki
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from thefuzz import fuzz

wikipedia = MediaWiki()
athletelist = ['Lionel Messi', 'Christiano Ronaldo', 'Mohamed Salah', 'Sadio Mane', 'Marcus Rashford', 'Son Heung-Min', 'Christian Pulisic', 'Kylian Mbappé', 'Robert Lewandowski', 'David Beckham', 'Neymar', 'Pelé', 'Diego Maradona', 'Zinedine Zidane']

def pullinfo(athlete):
    """Function goes through and pulls the wikipedia page for each player on the athlete list""" 
    player = wikipedia.page(athlete)
    playerinfo = player.summary
    return playerinfo

def removepunc(string):
    """Function removes punctuation from the articles pulled from Wiki"""
    punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    
    for c in string:
        if c in punc:
            string = string.replace(c, "")
    return string
    
def listconv(z):
    """Takes the newly punctionuationless string and converts it into a list of individual words"""
 
    listofwords = list(z.split())
    return listofwords

def removecommons(y):
    """Removes a bunch of common words that don't really provide much insight"""
    common = ['also', 'born', 'as', 'is', 'an', 'who', 'for', 'club', 'and', 'the', 'in', 'of', 'to', 'he', 'had', 'his', 'was', 'with', 'where', 'a', 'by']
    nocommons = [x for x in y if x not in common]
    return nocommons


def most_pop(x):
    """Goes through the list for each player and counts how many times it is said, prints out the result if it is 5 or more"""
    d = dict()
    e = dict()
    for c in x:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    for key, value in d.items():
        if value >= 5:
            e[key] = value
    return e


# def top15(l):
#     """Goes through the whole dictionary of values and displays the highest 15 for each player
# Leaving this function here because I spent so many hours trying to get this to work, I was trying
# to take the dict created in the above function and print out the top 15 most popular words on each players page 
# but for the life of me I could not figure out how to do it, I ended up just making every word that showed up more than 5 times appear in the above function
# """

    # sortedvalues = sorted(l.values())
    # sorted_dict ={}
    # print(sortedvalues[-15:-14])
    # x = 0
    # for i in sortedvalues:
    #     for k in l.keys():
    #         if l[k] == i:
    #             sorted_dict[k] = l[k]
    # print(sorted_dict)
    # # print(dict(list(sorted_dict.items())[-1:-14]))
                      

def pullsent(athlete):
    """Pulls the whole wikipedia page for each player for sentiment analysis"""
    player = wikipedia.page(athlete)
    playercomp = player.content
    return playercomp

def sentscore(playercomp):
    scores = SentimentIntensityAnalyzer().polarity_scores(playercomp)
    return scores


def similarity(player1, player2):
    player1page = wikipedia.page(player1)
    player1info = player1page.summary
    player2page = wikipedia.page(player2)
    player2info = player2page.summary
    x = fuzz.ratio(player1info, player2info)
    print ('The similarity between the summaries of', player1, 'and', player2, 'is', x)



def main():

    #     #All the functions to do everything for the sentiment analysis
    # allscores = []
    # for athlete in athletelist:
    #     playercomp = pullsent(athlete)
    #     allscores.append(sentscore(playercomp))
    # fullscores = dict(zip(athletelist, allscores))
    # print ("{:<20} {:<10}".format('Athlete', 'Results'))
    # for item in fullscores:
    #     print(item, fullscores[item])
        
    # summaryscores = []
    # for athlete in athletelist:
    #     playersum = pullinfo(athlete)
    #     summaryscores.append(sentscore(playersum))
    # fullsumsco = dict(zip(athletelist, summaryscores))
    # print ("{:<20} {:<10}".format('Athlete', 'Results (Summary Only)'))
    # for item in fullsumsco:
    #     print(item, fullsumsco[item])

  #  All the functions that pull the data, clean it, analyze it and tell us the most common
    # for athlete in athletelist:
    #     playerinfo = pullinfo(athlete)
    #     cleanplayerinfo = removepunc(playerinfo)
    #     infolist = listconv(cleanplayerinfo)
    #     nocommons = removecommons(infolist)
    #     wordlist = most_pop(nocommons)
    #     print(athlete, wordlist)
    # Code to compare text similarities

    similarity('Lionel Messi', 'Christiano Ronaldo')
    similarity('Neymar', 'Diego Maradona')
    similarity('Robert Lewandowski', 'Christian Pulisic')
    similarity('Diego Maradona', 'Son Heung-Min')
    similarity('Sadio Mane', 'Mohamed Salah')
    similarity('Neymar', 'Pelé')
    similarity('Lionel Messi', 'Diego Maradona')
    similarity('Kylian Mbappé', 'Neymar')

   
    



if __name__ == "__main__":
    main()