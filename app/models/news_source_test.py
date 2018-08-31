import unittest
from models import news_source

News_Source = news_source.News_Source

class NewsTest(unittest.TestCase):
    '''
    Test class to test the behaviour of the news source class
    '''

    def setUp(self):
        '''
        Method to run before every test
        '''
        self.new_news_source = News_Source('abc-news', 'ABC News', 'Your trusted source for breaking news, analysis, exclusive interviews, headlines, and videos at ABCNews.com.', 'http://abcnews.go.com/', 'en', 'us')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_news_source,News_Source))

if __name__ == '__main__':
    unittest.main()            