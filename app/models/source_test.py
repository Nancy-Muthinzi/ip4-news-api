import unittest
from models import news_source

News_Source = news_source.News_Source

class SourceTest(unittest.TestCase):
    '''
    Test class to test the behaviour of the source class
    '''

    def setUp(self):
        '''
        Method to run before every test
        '''
        self.new_source = Source('abc-news', 'ABC News', 'Your trusted source for breaking news, analysis, exclusive interviews, headlines, and videos at ABCNews.com.', 'http://abcnews.go.com/', 'general', 'en', 'us')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_source, Source))

if __name__ == '__main__':
    unittest.main()            