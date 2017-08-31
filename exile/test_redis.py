import redis
rs = redis.Redis("192.168.1.6")
 
try:
    response = rs.client_list()
    print "its Ok.", response
except redis.ConnectionError:
    print "redis instance is down."