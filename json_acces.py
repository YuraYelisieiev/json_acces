import urllib.request, urllib.parse, urllib.error
import twurl
import json
import ssl
TWITTER_URL = 'https://api.twitter.com/1.1/friends/list.json'

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


# function to analyze friends information
# Recommended parameters(name, id, location, time_zone, friends_count, followers_count, lang)
def json_acces(user_param, number_friends):
    """
    (str, int) -> dict
    :param user_param:
    :param number_friends:
    :return:
    """
    friends_dict = {}
    acc = input('Enter Twitter Account: ')
    if (len(acc) < 1): return -1
    url = twurl.augment(TWITTER_URL,
                        {'screen_name': acc, 'count': number_friends})
    connection = urllib.request.urlopen(url, context=ctx)
    data = connection.read().decode()
    js = json.loads(data)
    for u in js['users']:
        print(u)
        s = u[user_param]
        friends_dict[u['screen_name']] = s
    return friends_dict
