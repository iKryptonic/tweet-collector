###
#Function to get a list of names from a file, returns a list with the names
#@param {string} exclude_file - path to file that has user names to exclude, one name per line
###
def getExclusionListFromFile(exclude_file):
    exclusion_list = []
    with open(exclude_file, 'r') as f:
            lines = f.readlines()

            for line in lines:
                #append names from file to exclusion_list and strip newlines
                exclusion_list.append(line.strip('\n'))

            f.close()
    return exclusion_list
    
###
#Function to remove tweets with specific usernames from data file
#@param {string} data_file - path to desired data file
#@param {string} exclude_file - path to file that has user names to exclude, one name per line
#@param {string list} exlusion_list - list of username string to exclude
###
def removeDesiredTweets(data_file, exclude_file=None, exclusion_list = None):
    #if no list is passed, a path to a file should be passed
    if exclusion_list is None:
        exclusion_list = getExclusionListFromFile(exclude_file)

    with open(data_file, 'r') as f:
        lines = f.readlines()
    with open(data_file, 'w') as f:
        for line in lines:
            #tokenize
            tweets = line.split(",")
            #usernames exists at position 0, check if in exclusion_list
            if tweets[0] not in exclusion_list:
                f.write(line)
                #print()
            else:
                #username of tweet that was removed
                print(tweets[0])
    f.close()

###-----------------------------------------------------------------------
#Remove official accounts from file
def removeOfficialAccountsFromFile(data_file, exclude_file = None, exclusion_list = None):
    
    #if no list is passed, a path to a file should be passed
    if exclusion_list is None:
        exclusion_list = getExclusionListFromFile(exclude_file)
        
    with open(data_file, 'r') as f:
        lines = f.readlines()
    with open(data_file, 'w') as f:
        for account_name in lines:
            if account_name.strip("\n") not in exclusion_list:
                f.write(account_name)
            else:
                print(account_name)
    f.close()