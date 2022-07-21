import datetime
import pandas as pd
import random
import numpy as np
from Forum_Page import *

#Do not change the lists below 
title_list = ['A Post', 'Final_Project', 'Potato_Recipe', 'Sea Turtle', 'The turtle moves']
post_text_list = ['This post is about nothing', 'You are working on the CSCI 140 Final Project', 'There \
are lots of ways to make potatoes', 'Sea Turtles migrate during different seasons', 'This is probably \
a Terry Pratchett reference']
#Write your main program code here

CSCI_140 = Forum_Page("CSCI_140") #Creates a Forum Page object called CSCI_140
for i in range(0, 5): #For loop that goes from 0-4 (loops 5 times)
    CSCI_140.add_post(title = title_list[i], post = post_text_list[i]) #Each loop it adds a post to the dataframe with i representing the list indexies
for i in range(0,3): #For loop that goes from 0-3 (loops 3 times)
    CSCI_140.vote_post("Final_Project", True) #Each loop it up votes "Final_Project"
print(CSCI_140.top_voted()) #Prints out the top voted post
print()
CSCI_140.delete_post("Potato_Recipe") #Deletes the "Potato_Recipe" post
print(CSCI_140.get_titles()) #Prints out a list of all the titles in the dataframe
print()
print(CSCI_140) #Prints of the str representation of the class
#print(CSCI_140.checker())