# Import necessary libraries
from flask import Flask, request, jsonify  # Flask for web API, request to handle incoming requests, jsonify to return JSON response
import pandas as pd  # pandas for data manipulation

# Starting Flask application
app = Flask(__name__)

# Read the Twitter dataset (TSV file )
df  = pd.read_csv('correct_twitter_201904.tsv', sep='\t')

# Display information about the dataframe
print(df.info())

# Check for missing values in each column
df.isnull().sum()

# Remove missing data
df.dropna(inplace=True)


# Convert the 'created_at' column to datetime format and handle any errors
df['created_at'] = pd.to_datetime(df['created_at'], errors='coerce', utc=True)

# Function to analyze tweets based on a search term
def analyze_tweets(df, Search_term):

    # Filter tweets that contain the search term (case-insensitive)
    filtered_df = df[df['text'].str.contains(Search_term, case=False, na=False)]
    
    # Get the number of tweets containing the term per day
    daily_counts = filtered_df.groupby(filtered_df['created_at'].dt.date)['id'].count()

    # Get the number of unique users who posted tweets containing the term
    unique_users = filtered_df['author_id'].nunique()

    # To Get the average likes for tweets containing the term
    avg_likes = filtered_df['like_count'].mean()

    # Get the locations (`place_id`) for tweets containing the term
    places = filtered_df['place_id'].unique()

    # Get the times of day when the tweets were posted
    filtered_df['Hour'] = filtered_df['created_at'].dt.hour
    tweet_times = filtered_df.groupby('Hour').size()

    # Get the users who posted the most tweets containing the term
    user_tweet_count = filtered_df.groupby('author_handle').size()
    max_tweet = user_tweet_count.max()
    top_users = user_tweet_count[user_tweet_count == max_tweet].index.tolist()


    # Return the results as a dictionary
    return {"daily_counts": daily_counts,
        "unique_users": unique_users,
         "Average_likes": avg_likes,
          "places": places,
           "Tweet_Times" : tweet_times,
            "Users_with_most_Tweets" : top_users }


# print(analyze_tweets(df,'Iron man'))

# Define the API route for analyzing tweets
@app.route('/analyze_tweets', methods=['GET'])
def analyze():
    # Get the search term from the query parameters
    Search_term = request.args.get('term')

    # If no search term is provided, return an error response
    if not Search_term:
        return jsonify({"error": "Please provide a search term using the 'term' query parameter."}),400
    
    # Call the analyze_tweets function and pass the search term
    result = analyze_tweets(df,Search_term)

    # Return the result as a JSON response
    return jsonify(result)

# Run the Flask application in debug mode
if __name__ == '__main__':
    app.run(debug=True)
