class News_Article:
    '''
    Class to define news article objects
    '''

    def __init__(self, id, name, author, title, description, url, url_to_image, publisher):
        
        self.id = id
        self.name = name
        self.author = author
        self.title = title
        self.description = description
        self.url = url
        self.url_to_image = url_to_image
        self.publisher = publisher
    
