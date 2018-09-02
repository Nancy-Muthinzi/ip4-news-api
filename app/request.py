from app import app
import urllib.request , json
from .models import source
from .models import article

Source = source.Source
Article = article.Article

# Getting api key
api_key = app.config['NEWS_API_KEY']

# Getting source url
source_url = app.config['NEWS_API_SOURCE_URL']

def get_source(category):
    '''
    Function to get json to respond to url request
    '''
    get_source_url=source_url.format(category, api_key)

    with urllib.request.urlopen(get_source_url) as url:
        get_source_data = url.read()
        get_source_response = json.loads(get_source_data)

        source_results = None

        if get_source_response['sources']:
            source_results_list = get_source_response['sources']
            source_results = process_results(source_results_list)

    return source_results  

def process_results(source_results_list):
    '''
    This function processes the source results and transfers them to a list of objects
    
    Args:
        source_list: list of dictionaties that contain news_source details

    Returns:
        source_results: list of source objects
    '''
    source_results = []
    for source_item in source_results_list:
        id = source_item.get('id')
        name = source_item.get('name')
        description = source_item.get('description')
        url = source_item.get('url')
        category = source_item.get('category')
        language = source_item.get('language')
        country = source_item.get('country')

        new_stuff = Source(id,name,description,url,category,language,country)
        source_results.append(new_stuff)

    return source_results        

def search_source(source_name):

    search_source_url = 'https://newsapi.org/v2/sources?category={}&apiKey={}'.format(api_key, source_name)
    with urllib.request.urlopen(search_source_url) as url:
        search_source_data = url.read()
        search_source_response = json.loads(search_source_data)

        search_source_results = None

        if search_source_response['sources']:
            search_source_list = search_source_response['sources']
            search_source_results = process_results (search_source_list)

            return search_source_results

#Getting article url
article_url = app.config['NEWS_API_ARTICLE_URL']

def get_article(category):
    '''
    Function to get json to respond to url request
    '''
    get_article_url=article_url.format(category,api_key)

    with urllib.request.urlopen(get_article_url) as url:
        get_article_data = url.read()
        get_article_response = json.loads(get_article_data)

        article_results = None

        if get_article_response['articles']:
            article_results_list = get_article_response['articles']
            article_results = process_results(article_results_list)

    return article_results        

def process_results(article_results_list):
    '''
    This function processes the articles results and transfers them to a list of objects
    
    Args:
        article_list: dictionaties that contain article details

    Returns:
        article_results: article objects
    '''
    article_results = []
    for article_item in article_results_list:
        id = article_item.get('id')
        name = article_item.get('name')
        author = article_item.get('author')
        title = article_item.get('title')
        description = article_item.get('description')
        url = article_item.get('url')
        urlToImage = article_item.get('urlToImage')
        publishedAt = article_item.get('publishedAt')

        if urlToImage:
            article_object = Article(id, name, author, title, description, url, publishedAt)
            article_results.append(article_object)

        return article_results  

def search_article(artice_name):

    search_article_url = 'https://newsapi.org/v2/everything?q={}&apiKey={}'.format(api_key, article_name)
    with urllib.request.urlopen(search_article_url) as url:
        search_article_data = url.read()
        search_article_response = json.loads(search_article_data)

        search_article_results = None

        if search_article_response['articles']:
            search_article_list = search_article_response['articles']
            search_article_results = process_results (search_article_list)

        return search_article_results        