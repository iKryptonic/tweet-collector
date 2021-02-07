'''
Created on Mar 27, 2015
Last modified on 05/19/2015

@author: Darina Dicheva / dichevad@wssu.edu
'''

import twitter
from twitter import TwitterError

api = twitter.Api(consumer_key='4Zw2UA9jbnY4LQuJD0zjjL3AM',
                      consumer_secret='xWgpVVFg69trN3CQbbpgpH4BWRAklu3DamHSAXBRlZc3vMMMJv',
                      access_token_key='3092759235-ZEh9p6h6oPAn6zXjysRBsje9B1yhtQGWw3U9OHw',
                      access_token_secret='CTeoMUTlyzrkNFmQzt7cTs0gsRUgzBJlBQ0ttjg8w3HAf')


punctuation="""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""
punctuationNoHashSymbol ="""!"$%&()*+,-./:;<=>?@[\]^_`{|}~"""       # without # and '

#-------------------------------------------------------------------------------
# Tokenizing a string and cleaning tokens; returns a list of clean tokens
def stringToTokens(tweetStr, punctuationStr):
    
    tokenList = tweetStr.split()    
    result=[]
    
    for i in range(0,len(tokenList),1):
        token = tokenList[i]
        cleaned = cleanToken(token, punctuationStr)
        result.append(cleaned)
        
    return result   
# end stringToTokens

#-------------------------------------------------------------------------------
# Cleaning a token; returns a string
def cleanToken(token, punctuationStr):

    cleaned = ""       
    if (not token.startswith("http")) and (not token.startswith("@")):           
        for i in range(0,len(token),1):
            if token[i] not in punctuationStr:
                cleaned += token[i]
   
    return cleaned.lower()   
# end stringToTokens

#-------------------------------------------------------------------------------

# Get WSSU related users and store their screen names in a file
def getWSSURelatedUsersNames(fname):
    
    uf = open(fname, 'w')
    userNameList = []   
    pageNum = 0         # which page of results to return
    
    while pageNum <= 50:
        print (pageNum)
        searchr =  api.GetUsersSearch("WSSU", page = pageNum, count=100, include_entities=False) # 50 and 100 are the max numbers that can be given
        for s in searchr:
            try:
                uname = s.screen_name
                #print  (str(uname))
                if not uname in userNameList:
                    print ("not in userList")
                    print  (str(uname))
                    userNameList.append(uname)
                    uf.write(str(uname) + "\n")
                print (pageNum)
                
            except UnicodeEncodeError:
                print (TwitterError.message)
                
        pageNum += 1
     
    print ()   
    print ("Users Name: "  + str(len(userNameList)) )         
    uf.close()

#-------------------------------------------------------------------------------
# Get the tweets of the users with screen names in file userNamesFile; store the text of the tweets along with other information in a file
def getCleanTweetsByUserNames(userNamesFile, tweetsFile):
       
    f = open(tweetsFile, 'w')    
    usersList = []
    tweetsNumber = 0
    
    # Get users screen names from the file
    with open(userNamesFile) as usersfile:
        for user in usersfile:
            user = user.replace("\n", "")   #remove end of line            
            usersList.append(user) 
    
    index = 0           
    while index < len(usersList):        
        userName = usersList[index]   
        print (index)
        try:
            userTweets = api.GetUserTimeline(screen_name=userName, count=200 )  #200 is the max allowed in the API
                
            for s in userTweets:                 
                # clean tokens in tweeet text
                tweetText = s.text
                tokenList = tweetText.split()
                cleanedText=""
                
                for i in range(0,len(tokenList),1):
                    token = tokenList[i]
                    cleanedToken = cleanToken(token, punctuationNoHashSymbol)
                    cleanedText = cleanedText + cleanedToken + " "
        
                line = userName + "\t" + str(s.id) + "\t" + str(s.created_at) + "\t" + str(s.retweet_count) + "\t" + cleanedText + "\n"
                f.write(line)
                print (line )              
                tweetsNumber += 1
     
        except UnicodeEncodeError:
            pass
        except TwitterError:
            pass
        
        index += 1  
        
    print ("Total Tweets Number: "  + str(tweetsNumber))
    print ("Users Number:        "  + str(len(usersList)))
    f.close()
     
# end getTweetsByUserNames()

#-------------------------------------------------------------------------------
# Merge two files containing 'full' tweets 
# Output a file containing full tweets and a file containing just the text of the tweets
def tweetFilesMerge (f1, f2, f3, f4):

    mergedStatusFile = open(f3, 'w')
    mergedTweetFile = open(f4, 'w')    
    tweetids = []

    # Get statuses from file 1
    num_tweets1 = 0
    with open(f1) as f1_statuses:
        for status in f1_statuses:
            uid, tweetid, dtime, rt, tweet = status.split("\t")
            # check if this tweet is already in the list, if not add it
            if not tweetid in tweetids:
                tweetids.append(tweetid)
                mergedStatusFile.write(status) 
                mergedTweetFile.write(tweet)                  
            num_tweets1 += 1
        
    # Get statuses from file 2
    num_tweets2 = 0
    with open(f2) as f2_statuses:
        for status in f2_statuses:
            uid, tweetid, dtime, rt, tweet = status.split("\t")
            # check if this tweet is already in the list, if not add it
            if not tweetid in tweetids:
                tweetids.append(tweetid)
                mergedStatusFile.write(status)
                mergedTweetFile.write(tweet)      
                num_tweets2 += 1
             
    print ("Number of tweets in file 1: " + str(num_tweets1))
    print ("Number of tweets in file 2: " + str(num_tweets2))
    print ("Number of tweets in merged files:  " + str(len(tweetids)))
    mergedStatusFile.close()
    mergedTweetFile.close()
    
# end of tweetFilesMerge()

#-------------------------------------------------------------------------------
# Merge two files containing user screen names in a third file, which does not contain duplicates 
def tweetUsersMerge (file1, file2, file3):

    f3 = open(file3, 'w')    
    userList = []

    # Get users from file 1
    n1 = 0
    with open(file1) as f1_users:
        for user in f1_users:
            n1 += 1
            if not user in userList:
                userList.append(user)      

    # Get users from file 2
    n2 = 0
    with open(file2) as f2_users:
        for user in f2_users:
            n2 += 1
            if not user in userList:
                userList.append(user)      
        
    for user in sorted(userList):
        try:
            f3.write(user)
            
        except UnicodeEncodeError:
            print( TwitterError.message)

    f3.close()        
    print ("Number of users in file 1: " + str(n1))
    print ("Number of users in file 2: " + str(n2))
    print ("Number of users in merged file:  " + str(len(userList)))
    
# end of tweetFilesMerge()
           
#-------------------------------------------------------------------------------
def anonymizeFullTweetsFile(fullTweetsFile, anonymFile):
       
    f = open(anonymFile, 'w')    
    tweetsNumber = 0
    
    # Get users screen names from the file
    with open(fullTweetsFile) as statusfile:        
        user_dict = {} # a dictionary with key userName and value userID
        number = 1
        
        for tweet in statusfile:
            tweet = tweet.replace("\n", " ")   #remove end of line            

            # extract user name from status
            ind = tweet.find("\t")      
            userName = tweet[:ind]

            # add user name to dictionary if not there
            if not userName in user_dict:
                user_dict[userName] = "UID"+str(number)
                number = number + 1
           
            fullTweet =  user_dict[userName] + tweet[ind:] + "\n"
            f.write(fullTweet)             
            tweetsNumber += 1
            
    f.close()
    print ("Total Tweets Number: "  + str(tweetsNumber))     
    
# end anonymizeFullTweetsFile() 
