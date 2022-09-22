import redis
redis = redis.Redis(host= '127.0.0.1', port= 6379, db= 0)  # Connecting to redis
key = input("Select Key to edit: ")                        # Key to alter
value = input("Input new Key value: ")                     # Value to alter 
redis.set (key, value)                                     # Altering value
tstky = redis.get (key)                                    # testing new key
tst = input("test? y/n: ")                                 # test new key?
if tst in ['y']:                                           # ^ ^ ^
    print(tstky)
if tst in ['n']:                                           # ^ ^ ^
    print("Ok")