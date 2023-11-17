from instabot import Bot
import os
import glob

bot = Bot()

def clearcookies():
    cookies = glob.glob("config/*cookie.json")
    for c in cookies:
        os.remove(c)
clearcookies()
bot.login(username = "WRITEYOURUSERNAME", password = "WRITEYOURPASSWORD") 

import locale
locale.setlocale(locale.LC_ALL, 'Turkish_Turkey.1254')
from datetime import datetime
t = datetime.today()
print(datetime.strftime(t, "%c"))

followers = bot.get_user_followers("qwertyu") #YOU CAN CHANGE THIS WHATEVER YOU WANT
print("----FOLLOWERS----")
ordinalNumber = 0
for follower in followers:
    ordinalNumber += 1
    print(str(ordinalNumber) + " ---> " + bot.get_username_from_user_id(follower))

following = bot.get_user_following("spursofficial") #YOU CAN CHANGE THIS WHATEVER YOU WANT
print("----FOLLOWING----")
ordinalNumber = 0
for following in following:
    ordinalNumber += 1
    print(str(ordinalNumber) + " ---> " + bot.get_username_from_user_id(following))
