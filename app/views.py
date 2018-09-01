from flask import render_template
from app import app
from .request import get_source, search_source
# from .request import get_article


# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
     #get sources
    source_general = get_source('general')
    # print(sources)

    title = 'Home - Welcome to the most informative news site online!!!'
    return render_template('index.html', title = title, general = source_general)

@app.route    

    #get articles
    # everything_articles = get_article()
    # print(everything)

    # title = 'Home - Welcome to the most informative news site online!!!'
    # return render_template('index.html', title = title, everything = everything)

   

@app.route('/news/<int:news_id>')
def news(news_id):

    '''
    View news page function that returns the news details page and its data
    '''
    return render_template('news.html',id = news_id)