**Twitter Data Analysis with API**

This is a Flask-based API for analyzing a dataset of tweets. The API allows you to filter tweets by a search term and returns analysis results like the number of tweets per day, the number of unique users, average likes, and more.

## Getting Started
Install necessary Python libraries pandas and flask

Download the Python file (SilverSpace_Project.py) to your local machine.

Ensure you have the dataset correct_twitter_201904.tsv in the same directory as the Python script.

Run the Flask Application:

Navigate to the folder where you have saved your Python script in your terminal or command prompt.
Run the following command:
python SilverSpace_Project.py

## Access the API:

After running the script, you will see a message like:
csharp
Copy code
Running on http://127.0.0.1:5000/
Open a web browser:
http://127.0.0.1:5000/analyze_tweets?term=<your_search_term>
Replace <your_search_term> with the word or phrase you want to search in the tweets.

Example Request
To analyze tweets containing the term "Marvel" you can use the following URL:

http://127.0.0.1:5000/analyze_tweets?term=Marvel
