import unittest
from Forum_Page import *

class Functions_Tester(unittest.TestCase):
    
    def setUp(self):
        self.__forumpage = Forum_Page('Baking')
        self.__words = self.__forumpage._Forum_Page__anon_words
    
    def test_generate_post_anon(self):
        print('\nTesting generate_post_anon')
        try:
            self.__forumpage.add_post('Savoury', 'Quiche')
            current = self.__forumpage.checker()
            print('Internal data frame contains:')
            print(current)
            author_item = current.loc['Savoury','Author'].split('_')
            print('Checking format and content of anonymous author')
            self.assertTrue(author_item[0] in self.__words and author_item[1] in self.__words and author_item[2].isdigit())
        except BaseException as e:
            print('Testing failed')
            print(e)
        
  
    def test_add_post_multiple(self):
        print('\nAdding posts to the forum')
        try:
            self.__forumpage.add_post('Savoury', 'Quiche', author = 'Aarolicious')
            self.__forumpage.add_post('Sweet', 'Cakes', author = 'Sweetypie')
            self.__forumpage.add_post('No_Category', 'Random', author = 'AnonBaker')
            current = self.__forumpage.checker()
            print('Internal data frame contains:')
            print(current)
            expected = pd.read_csv('result1.txt',index_col = 0)
            expected['Date'] = expected['Date'].apply(lambda x: str(datetime.date.today()))
            expected['Votes'] = expected['Votes'].astype(int)
            print('Expected:')
            print(expected)
            print('Checking for equal content of data frames')
            self.assertTrue(current.eq(expected).all().all())
        except BaseException as e:
            print('Testing failed')
            print(e)

            
            
    def test_delete_post_there(self):
        print('\nTesting delete_post_there')
        try:
            self.__forumpage.add_post('Savoury', 'Quiche', author = 'Aarolicious')
            self.__forumpage.add_post('Sweet', 'Cakes', author = 'Sweetypie')
            self.__forumpage.delete_post('Savoury')
            current = self.__forumpage.checker()
            print('Internal data frame contains:')
            print(current)
            expected = pd.read_csv('result4.txt',index_col=0)
            expected['Votes'] = expected['Votes'].astype(int)
            expected['Date'] = expected['Date'].apply(lambda x: str(datetime.date.today()))
            print('Expected:')
            print(expected)
            print('Checking for equal content of data frames')
            self.assertTrue(current.equals(expected))
        except BaseException as e:
            print('Testing failed')
            print(e)
    
    def test_delete_post_not_there(self):
        print('\nTesting delete_post_not_there')
        try:
            self.__forumpage.add_post('Savoury', 'Quiche', author = 'Aarolicious')
            self.__forumpage.add_post('Sweet', 'Cakes', author = 'Sweetypie')
            cur_frame = self.__forumpage.checker()
            self.__forumpage.delete_post('No Category')
            expected = pd.read_csv('result5.txt',index_col = 0)
            expected['Votes'] = expected['Votes'].astype(int)
            expected['Date'] = expected['Date'].apply(lambda x: str(datetime.date.today()))
            self.assertTrue(self.__forumpage.checker().eq(expected).all().all())
        except BaseException as e:
            print('Testing failed')
            print(e)
     
    
    
    def test_vote_post(self):
        print('\nTesting vote_post')
        try:
            self.__forumpage.add_post('Savoury', 'Quiche', author = 'Aarolicious')
            self.__forumpage.add_post('Sweet', 'Cakes', author = 'Sweetypie')
            self.__forumpage.add_post('No_Category', 'Random', author = 'AnonBaker')
            self.__forumpage.vote_post('Savoury')
            self.__forumpage.vote_post('Savoury')
            self.__forumpage.vote_post('Savoury')
            self.__forumpage.vote_post('Sweet')
            self.__forumpage.vote_post('Sweet', up = False)
            self.__forumpage.vote_post('Sweet')
            self.__forumpage.vote_post('Sweet', up = False)
            current = self.__forumpage.checker()
            print('Internal data frame contains:')
            print(current)
            expected = pd.read_csv('result2.txt',index_col = 0)
            expected['Votes'] = expected['Votes'].astype(int)
            expected['Date'] = expected['Date'].apply(lambda x: str(datetime.date.today()))
            print('Expected:')
            print(expected)
            print('Checking for equal content of data frames')
            self.assertTrue(current.eq(expected).all().all())
        except BaseException as e:
            print('Testing failed')
            print(e)
            
            
    def test_top_voted(self):
        print('\nTesting top_voted')
        try:
            self.__forumpage.add_post('Savoury', 'Quiche', author = 'Aarolicious')
            self.__forumpage.add_post('Sweet', 'Cakes', author = 'Sweetypie')
            self.__forumpage.add_post('No_Category', 'Random', author = 'AnonBaker')
            self.__forumpage.vote_post('Savoury')
            self.__forumpage.vote_post('Savoury')
            self.__forumpage.vote_post('Savoury')
            self.__forumpage.vote_post('Sweet', up = True)
            self.__forumpage.vote_post('Sweet', up = False)
            self.__forumpage.vote_post('Sweet', up = True)
            self.__forumpage.vote_post('Sweet', up = False)
            top_voted_post = self.__forumpage.top_voted()
            print('Observed:')
            print(top_voted_post)
            print('Expected:')
            expected = pd.read_csv('result3.txt').set_index('Title')
            expected['Date'] = expected['Date'].apply(lambda x: str(datetime.date.today()))
            expected['Votes'] = expected['Votes'].astype(int)
            print(expected)
            self.assertTrue(top_voted_post.eq(expected).all().all())
        except BaseException as e:
            print('Testing failed')
            print(e)     
            
            
    def test_get_titles(self):
        print('\nTesting get_titles')
        try:
            self.__forumpage.add_post('Savoury', 'Quiche', author = 'Aarolicious')
            self.__forumpage.add_post('Sweet', 'Cakes', author = 'Sweetypie')
            self.__forumpage.add_post('No_Category', 'Random', author = 'AnonBaker')
            titles = self.__forumpage.get_titles()
            self.assertEqual(titles, ['Savoury', 'Sweet', 'No_Category'])
        except BaseException as e:
            print('Testing failed')
            print(e)        
            
    
    def test_get_post_info(self):
        print('\nTesting get_post_info')
        try:
            self.__forumpage.add_post('Savoury', 'Quiche', author = 'Aarolicious')
            info = self.__forumpage.get_post_info('Savoury')
            self.assertEqual(info, [str(datetime.date.today()),'Aarolicious','Quiche',0])
        except BaseException as e:
            print('Testing failed')
            print(e)    
            
    def test__str__(self):
        print('\nTesting __str__')
        try:
            self.__forumpage.add_post('Savoury', 'Quiche', author = 'Aarolicious')
            self.__forumpage.add_post('Sweet', 'Cakes', author = 'Sweetypie')
            self.__forumpage.add_post('No_Category', 'Random', author = 'AnonBaker')
            observed = str(self.__forumpage)
            print('Observed:')
            print(observed)
            print('Expected:')
            expected = '3 active posts on Baking'
            print(expected)
            self.assertEqual(observed, expected)
        except BaseException as e:
            print('Testing failed')
            print(e) 
            
            
  
    
if __name__ == '__main__':
    unittest.main()

