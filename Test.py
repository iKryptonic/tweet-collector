import twitter
from twitter import TwitterError

api = twitter.Api(consumer_key='4Zw2UA9jbnY4LQuJD0zjjL3AM',
                      consumer_secret='xWgpVVFg69trN3CQbbpgpH4BWRAklu3DamHSAXBRlZc3vMMMJv',
                      access_token_key='3092759235-ZEh9p6h6oPAn6zXjysRBsje9B1yhtQGWw3U9OHw',
                      access_token_secret='CTeoMUTlyzrkNFmQzt7cTs0gsRUgzBJlBQ0ttjg8w3HAf')

print("here 1")

userNameList = []   

search = api.GetFollowerIDs(user_id=None, screen_name=None, cursor=None, stringify_ids=False, count=None, total_count=None)
for s in search:
    try:
        #uname = s.GetScreenName()
        #print  (str(uname))
        print  (s)
        
    except UnicodeEncodeError:
        print (TwitterError.message)

# searchr = api.GetUsersSearch("WSSU", page=1, count=100, include_entities=False)  # 50 and 100 are the max numbers that can be given
# for s in searchr:
#     try:
#         uname = s.GetScreenName()
#         print  (str(uname))
#         if not uname in userNameList:
#             print ("not in userList")
#         userNameList.append(uname)
#                 
#     except UnicodeEncodeError:
#         print (TwitterError.message)
#                 
#      
#     print ()   
#     print ("Users Name: " + str(len(userNameList)))  
