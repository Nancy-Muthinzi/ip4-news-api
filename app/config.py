class Config:
    '''
    General configuration parent class
    '''
    # NEWS_API_KEY=''
    NEWS_API_ARTICLE_URL='https://newsapi.org/v2/top-headlines?country=us&apiKey={}'
    NEWS_API_SOURCE_URL='https://newsapi.org/v2/sources?apiKey={}'

class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass

class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True