'''
Created on Mar 27, 2015

@author: Darina Dicheva / dichevad@wssu.edu

'''
from TweetsAnalysisFunctions import percentOfRetweetedTeets, tweetsInCategoryCount, hashtagFrequencyFromFile, termFrequencyFromFile, createWordList 

# Tweets Categories
sportList = createWordList("files/CategorySport.txt")
technologyList = createWordList("files/CategoryTechnology.txt")
entertainmentList = createWordList("files/CategoryEntertainment.txt")
healthList = createWordList("files/CategoryHealth.txt")
diningList = createWordList("files/CategoryDining.txt")
financeList = createWordList("files/CategoryFinances.txt")
educationList = createWordList("files/CategoryTechnology.txt")
myUniversityList =createWordList("files/CategoryEducation.txt")
politicsList = createWordList("files/CategoryPoliticsLaw.txt")
religionList = createWordList("files/CategoryReligion.txt")

def main():
  
    #tweets_status = "files/t_1432072541.83_anonymFullTweets.txt"
    #tweets_text = "files/t_1432072541.83_allTweetsText.txt"
    tweets_status = input("Enter the name of the file with full tweets: ")
    tweets_text = input("Enter the name of the file tweets' text: ")

    done = False   
    while not done :
                        
        print (" ")
        print ("********************************************************") 
        print ("  1 - FIND THE NUMBER OF TWEETS IN SELECTED CATEGORIES")
        print ("  2 - FIND THE MOST USED TERMS ")
        print ("  3 - FIND THE MOST USED HASHTAGS")  
        print ("  4 - FIND PERCENT OF TWEETS THAT HAVE BEEN RE-TWEETED")     
        print ("  5 - EXIT")
        print ("********************************************************")
        
        choice = input("Enter your choice: ")  
        
        if choice == 1:
            # FIND THE NUMBER OF TWEETS IN SELECTED CATEGORIES
            tweetsByCategories(tweets_text)                
        elif choice == 2:
            # GET TERM FREQUENCIES
            termFrequencyFromFile(tweets_text)
        elif choice == 3:
            # GET HASHTAGS FREQUENCIES
            hashtagFrequencyFromFile(tweets_text)
        elif choice == 4:
            # GET HASHTAGS FREQUENCIES
            percentOfRetweetedTeets(tweets_status)
        elif choice == 5:
            print ("Bye ...")
            done = True
        else :
            print ("Enter a correct option")
    
    
    # FIND THE NUMBER OF TWEETS IN SELECTED CATEGORIES
def tweetsByCategories(tweetsFile):    
    tweets_count = tweetsInCategoryCount(tweetsFile, sportList) 
    print ("Tweets Count in Sports Category: " + str(tweets_count))
       
    # # Get the count of tweets in the Technology category
    tweets_count = tweetsInCategoryCount(tweetsFile, technologyList)
    print ("Tweets in Technology Category: " + str(tweets_count))
       
    # # Get the count of tweets in the Education category
    tweets_count = tweetsInCategoryCount(tweetsFile, religionList)
    print ("Tweets in Religion Category: " + str(tweets_count))
      
    # Get the count of tweets in the Politics category
    tweets_count = tweetsInCategoryCount(tweetsFile, politicsList)
    print ("Tweets in Politics Category: " + str(tweets_count))
     
    # Get the count of tweets in the Politics category
    tweets_count = tweetsInCategoryCount(tweetsFile, entertainmentList)
    print ("Tweets in Entertainment Category: " + str(tweets_count))
 
    # Get the count of tweets in the Politics category
    tweets_count = tweetsInCategoryCount(tweetsFile, healthList)
    print ("Tweets in Health & Wellness Category: " + str(tweets_count))
      
    # Get the count of tweets in the Politics category
    tweets_count = tweetsInCategoryCount(tweetsFile, educationList)
    print ("Tweets in Education Category: " + str(tweets_count))
    
    # Get the count of tweets in the Politics category
    tweets_count = tweetsInCategoryCount(tweetsFile, myUniversityList)
    print ("Tweets in myUniversity Category: " + str(tweets_count))
    
    # Get the count of tweets in the Politics category
    tweets_count = tweetsInCategoryCount(tweetsFile, diningList)
    print ("Tweets in Dining Category: " + str(tweets_count))

    # Get the count of tweets in the Finance category
    tweets_count = tweetsInCategoryCount(tweetsFile, financeList)
    print ("Tweets in Finance Category: " + str(tweets_count))


#-------------------------------------------------------------------------------
if __name__ == '__main__':
    main()
    
    