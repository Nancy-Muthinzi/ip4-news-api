from flask import render_template, request, redirect, url_for
from app import app
from .request import get_source, search_source
from .request import get_article, search_article


# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
     #get sources
    source_general = get_source('general')
    print(source_general)

    title = 'Home - Welcome to the most informative news site online!!!'

    search_source = request.args.get('search_query')

    if search_source:
        return redirect(url_for('search', source_name = search_source))

    else:    
        return render_template('index.html', title = title, general = source_general)

@app.route('/search/<source_name>')
def search(source_name):
    '''
    View function to display search results
    '''
    source_name_list = source_name.split(" ")
    source_name_format = "+".join(source_name_list)
    searched_sources = search_source(source_name_format)
    title = f'search results for {source_name}'

    return render_template('search.html', sources = searched_sources)

    #get articles
    article_general = get_article('general')
    article_business = get_article('business')
    article_technology = get_article('technology')
    article_sports = get_article('sports')

    title = 'Home - Welcome to the most informative news site online!!!'
    return render_template('index.html', title = title, general = article_general, business = article_business, technology = article_technology, sports = article_sports)

   

@app.route('/source/<int:id>')
def source(source_id):

    '''
    View news page function that returns the news details page and its data
    '''
    source = get_source(id)
    title = f'{source.title}'
    
    return render_template('source.html',id = source_id)