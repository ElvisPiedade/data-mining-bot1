import config
import pandas as pd
import tweepy

def getFollowersAndFriends(users):
	count = 0
	temp = 0
	for id_user in users.index: 
		followers = len(users['Followers'][id_user])
		friends = len(users['Friends'][id_user])
		
		users['Followers'][id_user] = [follower for follower in tweepy.Cursor(api.followers_ids, screen_name = users['ScreenName'][id_user], wait_on_rate_limit=True).items()]
		users['Friends'][id_user] = [friend for friend in tweepy.Cursor(api.friends_ids, screen_name = users['ScreenName'][id_user], wait_on_rate_limit=True).items()]

		if count == temp + 100:
			users.to_csv('new_users.csv', mode ='w')
			temp = count

		count+=1

	users.to_csv('new_users.csv', mode ='w')	


def read_file():
	df = pd.read_csv('users_info.csv', index_col = 0)
	return df

if __name__ == '__main__':

	auth = tweepy.OAuthHandler(config.CONSUMER_KEY, config.CONSUMER_SECRET)
	auth.set_access_token(config.ACCESS_KEY, config.ACCESS_SECRET)
	api = tweepy.API(auth)
	
	temp_df = read_file()
	getFollowersAndFriends(temp_df)
	