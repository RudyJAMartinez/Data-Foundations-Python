def file_to_set(file):
    """
    This function should take a file handler as input and return a set.
    
        Parameters:
            - file file handle: This variable is a file handle
            
        Return:
            - The file should return a set (e.g., {'good', 'great', 'happy'})
    """
    word_set = set()
    
    for word in file:
        word_set.add(word.strip())

    return word_set # You should return a set

positive_file = open('./bing_liu/positive-words.txt', encoding='utf8')
positive_words = file_to_set(positive_file)
positive_file.close()

negative_file = open('./bing_liu/negative-words.txt', encoding='iso-8859-1') # If you get a weird read error. Let me know. We can change the encoding.
negative_words = file_to_set(negative_file)
negative_file.close()



def count_sentiment_words(sentiment_set, tweet_text, lower):
    """
    This function takes a set and string as input, then counts the number of words that 
    appear in the string (tweet_text) that are also in the set (sentiment_set). The
    tweet_text should be normalized based on the lower argument (i.e., lowercase if True)
    
        Parameters:
            - sentiment_set set: A set of sentiment words, e.g., {'good', 'great', 'happy'}
            - tweet_text string: A tweet, e.g., "I go to UTSA!!!"
            - lower bool: A True or False boolean value indicating the tweet_text should be lowercased
    """
    word_count = 0
    
    for word in tweet_text.split():
        if word in sentiment_set:
            word_count += 1
    
    return word_count #You should return a number



def predict(num_pos_words, num_neg_words):
    """
    This function should return the string "positive", "negative", or "neutral" given
    the input parameters, i.e., if num_pos_words is greater than num_neg_words, return "positive"
    
        Parameters:
            - num_pos_words int: This is a count representing the number of positive words in a tweet.
            - num_neg_words int: This is a count representing the number of negative words in a tweet.
            
        Return:
            - Return a string "positive", "negative", or "neutral"
    """

    result = ['positive', 'negative', 'neutral']
    
    if num_pos_words - num_neg_words > 0:
        return result[0]
    elif num_pos_words - num_neg_words < 0:
        return result[1]
    else:
        return result[2]



def predict_score(num_pos_words, num_neg_words):
    """
    This function should generate a sentiment score num_pos_words - num_neg_words.
    
        Parameters:
            - num_pos_words int: This is a count representing the number of positive words in a tweet.
            - num_neg_words int: This is a count representing the number of negative words in a tweet.
            
        Return:
            - Return an integer representing the difference between positive words and negative words.
    """
    sentiment_score = int(num_pos_words - num_neg_words)
    
    return sentiment_score



import json

def json_string_to_dictionary(json_string):
    """
    This function should take a json string and convert it into a Python object (hint: loads)
    
        Parameters:
            - json_string str: A json string, e.g., '{"a": 1}'
            
        Returns:
            - Return a python object, e.g., {"a": 1} <--- look no quotes, so this is a dictionary
    """
    result = json.loads(json_string)
    return result



total_number_of_tweets = 0
total_number_of_positive_tweets = 0
total_number_of_negative_tweets = 0
total_number_of_users = 0
max_tweets = 0
user_with_most_tweets = ''

# Added Variables
unique_users = {}
total_number_of_neutral_tweets = 0
user_scores = {}
max_score = 0
min_score = 0



most_positive_tweet = ''
most_negative_tweet = ''
average_number_tweets_per_user = 0


# NOTE: You may need to define extra variables to help generate the required output.

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
    
    #   5. Keep track of the average number of tweets per user (how many tweets does each user make, on average)
    
    
    #   6. Keep track of the most positive and negative tweets.
    user_scores[screen_name] = user_scores.get(screen_name, 0) + sentiment_score
        
    ################################

# Total Count of Unique Users
total_number_of_users = len(unique_users)    
    
    
#   3. Keep track of the user that tweet the most
for k,v in unique_users.items():
    if v > max_tweets:
        max_tweets = v
        user_with_most_tweets = k

for k,v in user_scores.items():
    if v > max_score:
        max_score = v
        

twitter_dataset.close()


print(unique_users.items())
# print("Total Number of Tweets: {}".format(total_number_of_tweets))
# print("Total Number of Positive Tweets: {}".format(total_number_of_positive_tweets))
# print("Total Number of Negative Tweets: {}".format(total_number_of_negative_tweets))
# print("Total Number of Neutral Tweets: {}\n".format(total_number_of_neutral_tweets))
# print("Total Number of Users: {}".format(total_number_of_users))
# print("User with the most tweets: {}".format(user_with_most_tweets))
