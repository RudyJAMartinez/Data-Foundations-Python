total_number_of_tweets = 0
total_number_of_positive_tweets = 0
total_number_of_negative_tweets = 0
total_number_of_users = 0
max_tweets = 0
user_with_most_tweets = ''
most_positive_tweet = ''
most_negative_tweet = ''
average_number_tweets_per_user = 0

# Added Variables
unique_users = {}
total_number_of_neutral_tweets = 0
user_scores = {}
max_score = 0
min_score = 0

twitter_dataset = open('puerto-rico.jsonl', 'r')

for row in twitter_dataset:
    tweet_dict = json_string_to_dictionary(row)
    
    ###############################
    
    tweet_text = tweet_dict['full_text'] # MODIFY THIS LINE TO GET THE "full_text" from the tweet_dict
    screen_name = tweet_dict['user']['screen_name'] # MODIFY THIS LINE TO GET THE "screen_name" from the tweet_dict
    
    ###############################
    
    num_pos_words = count_sentiment_words(positive_words, tweet_text, True)
    num_neg_words = count_sentiment_words(negative_words, tweet_text, True)
    
    sentiment_prediction = predict(num_pos_words, num_neg_words)
    sentiment_score = predict_score(num_pos_words, num_neg_words)
    
    ################################
    
    #   1. Keep track of the number of tweets
    total_number_of_tweets += 1
        
    #   2. Keep track of the number of positive and negative tweets
    if sentiment_prediction == 'positive':
        total_number_of_positive_tweets += 1
    elif sentiment_prediction == 'negative':
        total_number_of_negative_tweets += 1
    else:
        total_number_of_neutral_tweets += 1
    
    #   4. Keep track of the total number of unique users
    unique_users[screen_name] = unique_users.get(screen_name, 0) + 1
    
    #   6. Keep track of the most positive and negative tweets.
    user_scores[tweet_text] = user_scores.get(tweet_text, 0) + sentiment_score
        
    ################################

# Total Count of Unique Users
total_number_of_users = len(unique_users)    
    
#   3. Keep track of the user that tweets the most
for k,v in unique_users.items():
    if v > max_tweets:
        max_tweets = v
        user_with_most_tweets = k

#   5. Keep track of the average number of tweets per user (how many tweets does each user make, on average)
average_number_tweets_per_user = total_number_of_tweets / total_number_of_users
        
# Most Positive and Negative Tweets
for k,v in user_scores.items():
    if v > max_score:
        max_score = v
        most_positive_tweet = k
    if v < min_score:
        min_score = v
        most_negative_tweet = k

twitter_dataset.close()