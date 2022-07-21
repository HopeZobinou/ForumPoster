import datetime
import pandas as pd
import random
import numpy as np

class Forum_Page:

    def __init__(self, name):
        self.__name = name
        self.__board = pd.DataFrame(columns = ['Title','Date', 'Author', 'Post', 'Votes'])
        self.__board.set_index('Title', inplace = True)
        self.__board['Votes'] = self.__board['Votes'].astype('int')
        self.__anon_words = self.__process('words.txt')
        
    
    def __process(self, filename):
        with open(filename,'r', encoding = 'UTF8') as file:
           result = [line.rstrip() for line in file]
        return result
        
    def __exists(self, title):
        return title in self.__board.index
    
    def checker(self):
        return self.__board.copy()
    
    def __generate_anon(self): 
        RandomWord = random.choices(self.__anon_words, k = 2) #Gets 2 unique random words
        RandomNum1 = random.choice(range(0,10)) #Gets a random number from 0-9
        RandomNum2 = random.choice(range(0,10)) #Gets a random number from 0-9
        RandomUserName = (RandomWord[0] + "_" + RandomWord[1] + "_" + str(RandomNum1) + str(RandomNum2)) #Makes the random username
        if RandomUserName in self.__board["Author"]: #Checks if the name is the same as other post
            self.__generate_anon() #Makes a new username
            return RandomUserName
        else:
            return RandomUserName
        
    def add_post(self, title, post, author = None):
        if  self.__exists(title) == True: #If the title is the same the other post
            return #Does nothing if it does
        elif author == None: #If the user doesn't give a name for the author
            self.__board.loc[title] = [str(datetime.date.today()), self.__generate_anon(), post, 0] #Then it generates a random name and adds the row to the dataframe(adds new post)
        else:
            self.__board.loc[title] = [str(datetime.date.today()), author, post, 0] #Adds a row to the data frame(adds new post)
            
    def delete_post(self, title):
        if self.__exists(title) == True: #If the title matches any titles in the forum
            MissingAuthor = self.__board.loc[title]["Author"] #Sets the value to a variable  
            MissingAuthor = np.nan #Sets the variable equal to nan and makes that value nan
            MissingPost = self.__board.loc[title]["Post"]
            MissingPost = np.nan
            self.__board.loc[title] = [str(datetime.date.today()), MissingAuthor, MissingPost, self.__board.loc[title]["Votes"]] #Deletes the post
            
    def vote_post(self, title, up = True):
        if self.__exists(title) == True and pd.isna(self.__board.loc[title]["Author"]) == False: #If the post exist and isn't deleted
            if up == True:
                UpVote = self.__board.loc[title]["Votes"] #Sets the vote to a variable
                UpVote += 1 #Adds one to the varaible making votes go up by one
                self.__board.loc[title] = [str(datetime.date.today()), self.__board.loc[title]["Author"], self.__board.loc[title]["Post"], UpVote] #Up votes the post
            elif up == False:
                DownVote = self.__board.loc[title]["Votes"] #Sets the vote to a variable
                DownVote -= 1 #Minus one to the variable making votes go down by one
                self.__board.loc[title] = [str(datetime.date.today()), self.__board.loc[title]["Author"], self.__board.loc[title]["Post"], DownVote] #Down votes the post
        else:
            return #Does nothing if the first condition isn't met
        
    def top_voted(self):
        MaxValue = self.__board["Votes"].max() #Gets the numerical value of the most amounts of votes
        return self.__board.loc[self.__board["Votes"] == MaxValue] #Returns the posts with the most amount of votes(positive) 
    
    def get_titles(self):
        return list(self.__board.index) #Returns a list of the titles in the dataframe
    
    def get_post_info(self, title):
        if self.__exists(title) == True: #Checks if the title is in the dataframe 
            return list(self.__board.loc[title]) #Returns a list of the post info
        else: #If the title doesn't exist
            return #Do nothing
                 
    def get_name(self):
        return self.__name
    
    def __str__(self):
        ActivePosts = 0 #Number of active posts
        for i in self.get_titles(): #For loop that goes through the list of titles
            if pd.isna(self.__board.loc[i]["Author"]) == False: #If the post doesn't have nan
                ActivePosts += 1 #Add one to ActivePosts count
        return str(ActivePosts) + " active posts on " + str(self.get_name()) #Retuns the number of active post and the name of the forum
    
    
a = Forum_Page("Reddit")
#print(a.__generate_anon())
a.add_post(title = "MW2019", post = "Worst COD ever", author = "Scope")
a.add_post(title = "NNN", post = "im not participating")
a.add_post(title = "NNN", post = "Im not a commer so yeh", author = "HOC")
a.add_post(title = "PSvXbox", post = "Both the same stop arguing", author = "Birdman")
a.add_post(title = "Kpop", post = "I love Kpop", author = "StanLuna")
a.delete_post(title = "Kpop")
a.vote_post(title = "MW2019", up = True)
a.vote_post(title = "MW2019", up = True)
a.vote_post(title = "Kpop", up = False)
a.vote_post(title = "NNN", up = True)
a.vote_post(title = "NNN", up = True)
print(a.top_voted())
print()
print(a.checker())
print()
print(a.get_titles())
print(a.get_post_info(title = "MW2019"))
print(a)
#s = pd.Series(["1","2","3"])
#s.loc[1] = np.nan
#print(s)