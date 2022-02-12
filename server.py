from flask import Flask,render_template,request
from TwitterScraper import scrape_tweets
import pandas as pd

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/twitter-data',methods=['POST','GET'])
def twitter_data():
    if request.method=='POST':
        # GETTING DATA FROM THE FORM
        no_of_tweets = request.form.get('no_of_tweets')
        no_of_tweets = int(no_of_tweets)
        start_date = request.form.get('startDate')
        end_date = request.form.get('endDate')
        keywords = request.form.getlist('keywords')

        # print(no_of_tweets,start_date,end_date,keywords)
        #PASSING DATA TO THE SCRAPER
        all_tweets = []
        for keyword in keywords:
            data = scrape_tweets(keyword,start_date,end_date,no_of_tweets)
            all_tweets.append(data)
        
        #FLATTENING THE NESTED LIST(RESULTS)
        flatten_list = [tweet for row in all_tweets for tweet in row]
        

        return render_template('twitter_results.html',data=flatten_list)
    else:
        return render_template('twitter_results.html')

if __name__=='__main__':
    app.run(host='127.0.0.1',port=5001,debug=True)

