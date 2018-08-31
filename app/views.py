from flask import render_template
from app import app
from .request import get_news_article
from .request import get_news_source

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    # #get news articles
    top_headlines_news_articles = get_news_article('top_headlines')
    print(top_headlines)

    title = 'Home - Welcome to the most informative news site online!!!'
    return render_template('index.html', title = title, top_headlines = top_headlines)

    #get news sources
    news_source = get_news_source('sources')
    print(sources)

    title = 'Home - Welcome to the most informative news site online!!!'
    return render_template('index.html', title = title, sources = sources)

# @app.route('/news/<int:news_id>')
# def news(news_id):

#     '''
#     View news page function that returns the news details page and its data
#     '''
#     return render_template('news.html',id = news_id)