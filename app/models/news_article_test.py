import unittest
from models import news_article

News_Article = news_article.News_Article

class NewsTest(unittest.TestCase):
    '''
    Test class to test the behaviour of the news articles class
    '''

    def setUp(self):
        '''
        Method to run before every test
        '''
        self.new_news_article = News_article()

    def test_instance(self):
        self.assertTrue(isinstance(self.new_news_article,News_Article))

if __name__ == '__main__':
    unittest.main()            