import redis                                             # importing redis
redis = redis.Redis(host= '127.0.0.1', port= 6379, db=0) # connecting to database
test = input("run test? y/n")                            # user prompt
success = redis.get ("test")                             # retrieving key from redis db
if test in ['y', 'Y', 'yes', 'Yes', 'YES']:              # checking user input
    print('success')                                     # ^ ^ ^
if test in ['n', 'N', 'no', 'No', 'NO']:                 # ^ ^ ^
    print('test canceled')                             # printing abort message