class News_Source:
    '''
    Class to define news source objects
    '''

    def __init__(self, id, name, description, url, category, languange, country):
        
        self.id = id
        self.name = name
        self.description = description
        self.url = url
        self.catergory = category
        self.language = languange
        self.country = country

