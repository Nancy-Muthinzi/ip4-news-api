from app import app
import urllib.request
import json
from .models import news_article
from .models import news_source

News_Article = news_article.News_Article
News_Source = news_source.News_Source

# Getting api key
api_key = app.config['NEWS_API_KEY']

#Getting news_article url
news_article = app.config["NEWS_API_ARTICLE_URL"]

def get_news_article(category):
    '''
    Function to get json to respond to url request
    '''
    get_news_article_url=news_article_url.format(category, api_key)

    with urllib.request.urlopen(get_news_article_url) as url:
        get_news_article_data = url.read()
        get_news_article_response = json.loads(get_news_article_data)

        news_article_results = None

        if get_news_article_response['results']:
            news_article_results_list = get_news_article_response['results']
            news_article_results = process_results(news_article_results_list)

    return news_article_results        

#Getting news_source url
news_source_url = app.config["NEWS_API_SOURCE_URL"]

def get_news_source(category):
    '''
    Function to get json to respond to url request
    '''
    get_news_source_url=news_source_url.format(category, api_key)

    with urllib.request.urlopen(get_news_source_url) as url:
        get_news_source_data = url.read()
        get_news_source_response = json.loads(get_news_source_data)

        news_source_results = None

        if get_news_source_response['results']:
            news_source_results_list = get_news_source_response['results']
            news_source_results = process_results(news_source_results_list)

    return news_source_results            