'''
Created on Mar 27, 2015
Last modified on May 14, 2015

@author: Darina Dicheva / dichevad@wssu.edu
'''
from TweetsExtractFunctions import stringToTokens
 
# Stop words from: http://xpo6.com/download-stop-word-list/
stopWordFile = "files/stop-word-list.txt" 
punctuation="""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""
punctuationNoHashSymbol ="""!"$%&()*+,-./:;<=>?@[\]^_`{|}~"""       # without # and '

number_returned = 50

# Read a file containing one word per line and return a list of the words; 
def createWordList(f):       
    word_list = []
    with open(f) as wordfile:
        for word in wordfile:
            word_list.append(word.replace("\n", ""))   #remove end of line
   
    return word_list     
    
#-------------------------------------------------------------------------------
# Create a dictionary from a list of tokens
def termFrequencyFromFile(txtFile):  
        
    stopWordList=createWordList(stopWordFile)  
    word_dict = {}
 
    with open(txtFile) as tweetsfile:
        # each tweet is one line
        for tweet in tweetsfile:
            wordList = stringToTokens(tweet, punctuation)
             
            for word in wordList:
                if (word) and (not word in stopWordList):
                    if not word in word_dict:
                        word_dict[word] = 1
                    else:
                        word_dict[word] += 1
         
    printFirstEntriesOfDictionary(word_dict, number_returned)
     
    return word_dict
    
#-------------------------------------------------------------------------------
# Prints the first 'number_returned' elements of a dictionary 
def printFirstEntriesOfDictionary(word_dict, number_returned):

    i = 0
    for key in sorted(word_dict, key=word_dict.get, reverse=True) :
        try:
            if i < number_returned :
                print (key, word_dict[key])
            i += 1
        except UnicodeEncodeError:
            print ("Twitter Error: UnicodeEncodeError")
    
# end printOrderedDictionary

#-------------------------------------------------------------------------------
#CREATE A DICTIONARY FROM A LIST OF TOKENS
def hashtagFrequencyFromFile(txtFile):     #  txtFile = "tweetsfile"
      
    hashtag_dict = {}
    with open(txtFile) as tweetsfile:
        # each tweet is one line
        for tweet in tweetsfile:
            wordList = stringToTokens(tweet, punctuationNoHashSymbol)
            
            for word in wordList:
                if word.startswith("#"):
                    # hashtag found, add to hashtag dictionary
                    if not word in hashtag_dict:
                        hashtag_dict[word] = 1
                    else:
                        hashtag_dict[word] += 1
                    
    printFirstEntriesOfDictionary(hashtag_dict, number_returned)
    
    return hashtag_dict

# hashtagFrequencyFromFile

#-------------------------------------------------------------------------------
# Create a dictionary of terms belonging to a category from a file of tweets 
def tweetsInCategoryCount(tweetsfile, categoryList):
          
    tweets_count = 0  
    total_tweets = 0 
    tweet_in_category = False 
    with open(tweetsfile) as tweetsfile:
        for tweet in tweetsfile:
            tweet_in_category = False
            tokenList = stringToTokens(tweet, punctuation)      
            
            for token in tokenList:                  
                if token in categoryList:
                    tweet_in_category = True
                    
            total_tweets = total_tweets + 1        
            if tweet_in_category:
                tweets_count = tweets_count + 1
                                
    return tweets_count 

#end categoryTermFrequency

#-------------------------------------------------------------------------------
# Get the percent of tweets that are re-tweets
def percentOfRetweetedTeets(tweetsFile):     
      
    retweets = 0.0
    tweets = 0

    with open(tweetsFile) as statusfile:
        for tstatus in statusfile: 
            tweets += 1       
            status = tstatus.replace("\n", "")   #remove end of line 
            uid, tweetid, dtime, retweet, tweet = status.split("\t")
            
            if int(retweet) > 0:
                retweets += 1

    print ("Number of tweets: " + str(tweets))
    print ("Number of tweets that are retweets: " + str(retweets))
    print ("Percent of retweeted tweets: " + str(retweets*100/tweets) + "%")

# percentOfRetweetedTeets
            