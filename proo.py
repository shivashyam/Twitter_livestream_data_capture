from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import time



#consumer key, consumer secret, access token, access secret.
ckey="kn02RmpS8B9hTKG3qErdPhBIZ"
csecret="5gR1udhDZ5tzLgk24mKAAiPMANac8IJvw2ubjdAD8pY2mNhExs"
atoken="563566303-Y5Ztmck0vJufcQtOt2xDWui2pQyaoPj7PMHvCo07"
asecret="SgqeJC9HaxrXiUxYgPT4HQevjJ9GJBnheLSRRduG0yvbw"

class listener(StreamListener):

    def on_data(self, data):
        try:
            print(data)
            tweet = data.split(',"text":"')[1].split('","source')[0]
            print(tweet)
            saveThis = str(time.time())+'::::'+tweet
            saveFile = open('data2.csv','a')
            saveFile.write(saveThis)
            saveFile.write('\n')
            saveFile.close()
            return(True)
        except:
            print("Failed", str(e))
            time.sleep(5)

    def on_error(self, status):
        print(status)

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

twitterStream = Stream(auth, listener())
twitterStream.filter(track=["car"])
