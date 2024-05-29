#import a module I made to handle twitter data
import twitter

#load the data from a twitter account
twitter_data = twitter.Account('BarackObama.csv')



# Variable for the tweet number
tweet_number = 0

# Print the tweet in the position
print(twitter_data[tweet_number].text)

# Print the likes of the tweet in the position
print(twitter_data[tweet_number].likes)

# Print the retweets of the tweet in the position
print(twitter_data[tweet_number].retweets)


# print the top 10 tweets
for i in range(10):
  print(twitter_data[i].text)


# --- Find the highest like count ---
max_likes = 0

for i in range(len(twitter_data)):
  if twitter_data[i].likes > max_likes:
    max_likes = twitter_data[i].likes

print("The tweet with the most likes has", max_likes, "likes")