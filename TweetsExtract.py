'''
Created on 03/27/2015
Last modified on 05/19/2015

@author: Darina Dicheva / dichevad@wssu.edu


'''
import time
from TweetsExtractFunctions import getWSSURelatedUsersNames, tweetUsersMerge, anonymizeFullTweetsFile
from TweetsExtractFunctions import tweetFilesMerge, getCleanTweetsByUserNames
from RemoveOfficialAccounts import removeDesiredTweets, removeOfficialAccountsFromFile


def main():

    # Set timestamps
    # The previous timestamp has to be entered manually
    previous_timestamp = "1613253691.2235389"
    current_timestamp = str(time.time())    # new stamp =             first current stamp = 1610655369.6565623
    print ("Previous timestamp: " + previous_timestamp)
    print ("Current timestamp: " + current_timestamp)
    
    # Users
    previous_users = "files/t_" + previous_timestamp + "_allUsers.txt"
    current_users = "files/t_" + current_timestamp + "_currentUsers.txt"
    merged_users = "files/t_" + current_timestamp + "_allUsers.txt"
    # Tweets
    previous_full_tweets = "files/t_" + previous_timestamp + "_allFullTweets.txt"
    current_full_tweets = "files/t_" + current_timestamp + "_currentFullTweets.txt"
    merged_full_tweets = "files/t_" + current_timestamp + "_allFullTweets.txt"
    merged_tweets_text = "files/t_" + current_timestamp + "_allTweetsText.txt"  
    anonym_full_tweets = "files/t_" + current_timestamp + "_anonymFullTweets.txt"
    
    exclusion_file = "files/WSSUOfficialAccountsToExclude.txt"
   
    done = False   
    while not done :
        
        print ("***************************************************************")
        print ("  1  - Continue")  
        print ("  2  - Exit" )
        print ("****************************************************************")
    
        choice = input("Enter your choice:  ")  
       
        if choice == '1':
            getWSSURelatedUsersNames(current_users)
            getCleanTweetsByUserNames(current_users, current_full_tweets)
            tweetUsersMerge (previous_users, current_users, merged_users)
            tweetFilesMerge (previous_full_tweets, current_full_tweets, merged_full_tweets, merged_tweets_text)
            anonymizeFullTweetsFile(merged_full_tweets, anonym_full_tweets)
            removeOfficialAccountsFromFile(merged_users, exclusion_file)
        elif choice == '2':
            print ("Bye ...")
            done = True
        else :
            print ("Enter a correct option")

#-------------------------------------------------------------------------------
if __name__ == '__main__':
    main()
    
